import json
import subprocess

import yaml


class YantramProcessor:
    LIFECYCLE_EVENT = 'lifecycle_event'
    DEPLOYMENTS = 'deployments'
    WORKSPACE = 'workspace'
    NAMESPACE = 'namespace'
    PROVIDER_CONFIGURATION = 'provider_configuration'
    DEPLOYMENT_CONFIGURATIONS = 'deployment_configurations'
    DEFAULT_PROVIDER_JSON = 'deployments/provider.json'
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
        bitnami = 'https://charts.bitnami.com/bitnami'
        prometheus_community = 'https://prometheus-community.github.io/helm-charts'
        grafana_community = 'https://grafana.github.io/helm-charts'

        with open(deployment_file) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            for datum in data['deployments']:
                configurations_ = datum['deployment_configurations']
                for configurations_key in configurations_:
                    with open(configurations_key) as f:
                        data = json.load(f)
                        for deployment_configuration in data['chart_configurations']:
                            chart = data['chart_configurations'][deployment_configuration]['chart']
                            if (bitnami == data['chart_configurations'][deployment_configuration]['repository']):
                                terraform_chart = ['helm', 'show', 'values', 'bitnami/' + chart, '--namespace',
                                                   'yantram']
                                self.download_chart(terraform_chart,
                                                    "inputs/defaults_chart_values/yantram-" + chart + '.yaml')
                            if (grafana_community == data['chart_configurations'][deployment_configuration][
                                'repository']):
                                terraform_chart = ['helm', 'show', 'values', 'grafana/' + chart, '--namespace',
                                                   'yantram']
                                self.download_chart(terraform_chart,
                                                    "inputs/defaults_chart_values/yantram-" + chart + '.yaml')
                            if (prometheus_community == data['chart_configurations'][deployment_configuration][
                                'repository']):
                                terraform_chart = ['helm', 'show', 'values', 'prometheus-community/' + chart,
                                                   '--namespace', 'yantram']
                                self.download_chart(terraform_chart,
                                                    "inputs/defaults_chart_values/yantram-" + chart + '.yaml')

    def download_chart(terraform_processes, taregt_file):
        # print("Downloading chart \t" + terraform_processes)
        print("Downloaded chart file : \t" + taregt_file)
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
