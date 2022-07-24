import json
import os
import subprocess
from pathlib import Path

import yaml

from apps.core.base.base_common import Base
from apps.core.processor.mongo_db_utils import MongoDBUtils

cwd = os.path.dirname(os.path.realpath(__file__))

class YantramProcessor(Base):
    def __init__(self):
        # super.__init__(self)
        self._LOGGER.debug("In YantramProcessor code")

    LIFECYCLE_EVENT = 'lifecycle_event'
    DEPLOYMENTS = 'deployments'
    WORKSPACE = 'workspace'
    NAMESPACE = 'namespace'
    PROVIDER_CONFIGURATION = 'provider_configuration'
    DEPLOYMENT_CONFIGURATIONS = 'deployment_configurations'
    DEFAULT_PROVIDER_JSON = 'deployment_configurations/provider.json'
    VAR_FILE_ = '-var-file='

    terraform_init = ["terraform", "init"]

    terraform_plan = ["terraform", "plan"]
    terraform_apply = ["terraform", "apply", "-auto-approve", "-lock=false"]
    terraform_refresh = ["terraform", "refresh", "-lock=false"]
    terraform_destroy = ["terraform", "destroy", "-auto-approve", "-lock=false"]

    terraform_workspace_new = ["terraform", "workspace", "new"]
    terraform_workspace_select = ["terraform", "workspace", "select"]
    terraform_workspace_select_default = ["terraform", "workspace", "select", "default"]
    terraform_workspace_delete = ["terraform", "workspace", "delete"]
    deployment_configuration = ["terraform", "workspace", "delete"]

    def download_charts(self,deployment_file):
        self._LOGGER.debug("Starting Chart Download %s",deployment_file)
        bitnami = 'https://charts.bitnami.com/bitnami'
        prometheus_community = 'https://prometheus-community.github.io/helm-charts'
        grafana_community = 'https://grafana.github.io/helm-charts'
        BASE_DIR = Path(cwd).resolve().parent.parent
        self._LOGGER.debug("BASE_DIR %s",BASE_DIR)
        dep = str(BASE_DIR) + "/static/" + deployment_file
        self._LOGGER.debug("deployment_file %s",dep)

        with open(dep) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            # self._LOGGER.debug("data %s", data)
            self._LOGGER.debug("configurations_key %s", data)

            for datum in data['deployments']:
                configurations_ = datum['deployment_configurations']
                for configurations_key in configurations_:
                    configurations_key_path = str(BASE_DIR) + "/static/" + configurations_key

                    with open(configurations_key_path) as f:
                        self._LOGGER.debug("configurations_key %s", configurations_key_path)
                        data = json.load(f)
                        self._LOGGER.debug("configurations_key %s", data)
                        for deployment_configuration in data['chart_configurations']:
                            chart = data['chart_configurations'][deployment_configuration]['chart']
                            self._LOGGER.debug("chart %s", chart)
                            chart_path = str(BASE_DIR) + "/static/defaults_chart_values/yantram-" + chart + '.yaml'
                            self._LOGGER.debug("chart_path %s", chart_path)

                            if (bitnami == data['chart_configurations'][deployment_configuration]['repository']):
                                terraform_chart = ['helm', 'show', 'values', 'bitnami/' + chart, '--namespace',
                                                   'yantram']
                                self._LOGGER.debug("chart %s", chart)
                                self.download_chart(terraform_chart,chart_path)
                            if (grafana_community == data['chart_configurations'][deployment_configuration][
                                'repository']):
                                terraform_chart = ['helm', 'show', 'values', 'grafana/' + chart, '--namespace',
                                                   'yantram']
                                self.download_chart(terraform_chart,chart_path)
                            if (prometheus_community == data['chart_configurations'][deployment_configuration][
                                'repository']):
                                terraform_chart = ['helm', 'show', 'values', 'prometheus-community/' + chart,
                                                   '--namespace', 'yantram']
                                chart_path = str(BASE_DIR) + "/static/defaults_chart_values/yantram-" + chart + '.yaml'
                                self.download_chart(terraform_chart,chart_path)
                                MongoDBUtils().save_helm_chart(chart_path)

    def core(self):
        yantram = YantramProcessor()
        YantramProcessor().invoke_process(yantram.terraform_init)
        output = {}
        with open('../../app-box/deployments.yaml') as inputDeploymentFile:
            deployment_file = yaml.load(inputDeploymentFile, Loader=yaml.FullLoader)
            namespace = deployment_file[yantram.NAMESPACE]
            deployments = deployment_file[yantram.DEPLOYMENTS]
            for deployment_module in deployments:
                lifecycle_event = deployment_module[yantram.LIFECYCLE_EVENT]
                deployment_configurations = deployment_module[yantram.DEPLOYMENT_CONFIGURATIONS]

                if yantram.PROVIDER_CONFIGURATION in deployment_module.keys():
                    # if deployment_module.has_key("provider_configuration"):
                    provider_configurations_file = deployment_module[yantram.PROVIDER_CONFIGURATION]
                else:
                    provider_configurations_file = yantram.DEFAULT_PROVIDER_JSON

                provider_configurations = yantram.VAR_FILE_ + provider_configurations_file
                workspace = namespace + "-" + deployment_module[yantram.WORKSPACE]

                terraform_apply = yantram.terraform_apply + [provider_configurations]
                terraform_refresh = yantram.terraform_refresh
                terraform_destroy = yantram.terraform_destroy + [provider_configurations]
                terraform_workspace_create = yantram.terraform_workspace_new + [workspace]
                terraform_workspace_select = yantram.terraform_workspace_select + [workspace]

                try:
                    if lifecycle_event == 'skip':
                        print("Skipping execution for deployment in workspace " + workspace)
                        continue

                    if lifecycle_event == 'create':
                        for deployment_configuration in deployment_configurations:
                            terraform_apply = terraform_apply + [yantram.VAR_FILE_ + deployment_configuration]
                        out_create_work = yantram.invoke_process(terraform_workspace_select)
                        if (out_create_work != 0):
                            out_create_work = yantram.invoke_process(terraform_workspace_create)
                        yantram.invoke_process(terraform_apply)
                        with open('terraform.tfstate.d/' + workspace + '/terraform.tfstate') as workspaceOut:
                            output[workspace] = json.load(workspaceOut)

                    if lifecycle_event == 'refresh':
                        terraform_refresh = terraform_refresh + [
                            yantram.VAR_FILE_ + 'terraform.tfstate.d/' + workspace + '/terraform.tfstate']
                        print(terraform_refresh)
                        out_create_work = yantram.invoke_process(terraform_refresh)
                        yantram.invoke_process(terraform_refresh)

                    if lifecycle_event == 'destroy':
                        for deployment_configuration in deployment_configurations:
                            terraform_destroy = terraform_destroy + [yantram.VAR_FILE_ + deployment_configuration]
                        terraform_workspace_delete = yantram.terraform_workspace_delete + [workspace]
                        yantram.invoke_process(terraform_destroy)
                        yantram.invoke_process(yantram.terraform_workspace_select_default)
                        yantram.invoke_process(terraform_workspace_delete)
                except Exception as e:
                    # Executerr().invoke_process(yantram.terraform_workspace_select_default)
                    # Executerr().invoke_process(terraform_workspace_delete)
                    return e
        return output

    def download_chart(self,terraform_processes, taregt_file):
        # print("Downloading chart \t" + terraform_processes)
        self._LOGGER.debug("Downloaded chart file : \t %s",taregt_file)
        p = subprocess.Popen(terraform_processes,
                             # cwd=cwd_m,
                             stdout=subprocess.PIPE)
        while True:
            output = p.stdout.readline().decode()
            if output == '' and p.poll() is not None:
                break
            if output:
                with open(taregt_file, "a+") as f:
                    f.write(output)
                    f.close()

        rc = p.poll()
        return rc

    def invoke_process(terraform_processes):
        p = subprocess.Popen(terraform_processes,
                             stdout=subprocess.PIPE)
        while True:
            output = p.stdout.readline().decode()
            if output == '' and p.poll() is not None:
                break
            if output:
                print(output.strip())

        rc = p.poll()
        # # with open('terraform.tfstate.d/kube/terraform.tfstate') as f:
        # #     data = json.load(f);
        # return data
        return rc
