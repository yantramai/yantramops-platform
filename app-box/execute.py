#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Jayant Kaushal <jayant@yantram.cloud>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import os
import subprocess
import json
import yaml

LIFECYCLE_EVENT = 'lifecycle_event'
DEPLOYMENTS = 'deployments'
WORKSPACE = 'workspace'
NAMESPACE = 'namespace'
PROVIDER_CONFIGURATION = 'provider_configuration'
DEPLOYMENT_CONFIGURATIONS = 'deployment_configurations'
DEFAULT_PROVIDER_JSON = 'deployments/provider.json'
VAR_FILE_ = '-var-file='


class executer:
    def core(self):
        self.invoke_process(self.terraform_init)
        output = {}
        with open('deployments.yaml') as inputDeploymentFile:
            deployment_file = yaml.load(inputDeploymentFile,Loader=yaml.FullLoader)
            namespace = deployment_file[NAMESPACE]
            deployments = deployment_file[DEPLOYMENTS]
            for deployment_module in deployments:
                lifecycle_event = deployment_module[LIFECYCLE_EVENT]
                deployment_configurations = deployment_module[DEPLOYMENT_CONFIGURATIONS]

                if PROVIDER_CONFIGURATION in deployment_module.keys():
                    # if deployment_module.has_key("provider_configuration"):
                    provider_configurations_file = deployment_module[PROVIDER_CONFIGURATION]
                else:
                    provider_configurations_file = DEFAULT_PROVIDER_JSON


                provider_configurations = VAR_FILE_ + provider_configurations_file
                workspace = namespace + "-" + deployment_module[WORKSPACE]

                terraform_apply = self.terraform_apply + [provider_configurations]
                terraform_refresh = self.terraform_refresh
                terraform_destroy = self.terraform_destroy + [provider_configurations]
                terraform_workspace_create = self.terraform_workspace_new + [workspace]
                terraform_workspace_select = self.terraform_workspace_select + [workspace]

                try:
                    print(lifecycle_event)

                    if (lifecycle_event == 'skip'):
                        print("Skipping execution for deployment in workspace "+workspace )
                        continue

                    if(lifecycle_event=='create'):
                        for deployment_configuration in deployment_configurations:
                            terraform_apply = terraform_apply + [VAR_FILE_+deployment_configuration]
                        out_create_work = executer().invoke_process(terraform_workspace_select)
                        if (out_create_work != 0):
                            out_create_work = executer().invoke_process(terraform_workspace_create)
                        self.invoke_process(terraform_apply)
                        with open('terraform.tfstate.d/'+workspace+'/terraform.tfstate') as workspaceOut:
                            output[workspace] = json.load(workspaceOut)

                    if(lifecycle_event=='refresh'):
                        terraform_refresh = terraform_refresh + [VAR_FILE_+ 'terraform.tfstate.d/'+workspace+'/terraform.tfstate']
                        print(terraform_refresh)
                        out_create_work = executer().invoke_process(terraform_refresh)
                        self.invoke_process(terraform_refresh)

                    if(lifecycle_event=='destroy'):
                        for deployment_configuration in deployment_configurations:
                            terraform_destroy = terraform_destroy + [VAR_FILE_+deployment_configuration]
                        terraform_workspace_delete = self.terraform_workspace_delete + [workspace]
                        self.invoke_process(terraform_destroy+['-force'])
                        self.invoke_process(self.terraform_workspace_select_default)
                        self.invoke_process(terraform_workspace_delete)
                except Exception as e:
                    # executer().invoke_process(self.terraform_workspace_select_default)
                    # executer().invoke_process(terraform_workspace_delete)
                    return e
        return output
    def download_charts(self):
        print("Downloading chart values for the users to configure...")
        repo_chart = ['helm', 'repo', 'update', '--namespace yantram']
        repo_ls = ['helm', 'ls', '--namespace', 'yantram']
        repo_chart = ['helm', 'repo', 'update']
        bitnami = 'https://charts.bitnami.com/bitnami'
        prometheus_community = 'https://prometheus-community.github.io/helm-charts'

        with open('../deployments.yaml') as f:
            data = yaml.load(f)
            for datum in data:
                with open(datum['deployment_configuration']) as f:
                    data = json.load(f);
                    for deployment_configuration in data['chart_configurations']:
                        chart = data['chart_configurations'][deployment_configuration]['chart']
                        print("Downloading chart \t"+chart)
                        if(bitnami == data['chart_configurations'][deployment_configuration]['repository']):
                            terraform_chart = ['helm', 'show', 'values','bitnami/'+chart, '--namespace', 'yantram']
                            executer().download_chart(terraform_chart,"inputs/defaults_chart_values/yantram-"+chart+'.yaml')
                        if(prometheus_community == data['chart_configurations'][deployment_configuration]['repository']):
                            terraform_chart = ['helm', 'show', 'values','prometheus-community/'+chart, '--namespace', 'yantram']
                            executer().download_chart(terraform_chart,"inputs/defaults_chart_values/yantram-"+chart+'.yaml')

    def invoke_process(self, terraform_processes):
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
    def download_chart(self, terraform_processes,taregt_file):
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

    def __init__(self):
        self.terraform_init = ["terraform", "init"]

        self.terraform_plan = ["terraform", "plan"]
        self.terraform_apply = ["terraform", "apply","-auto-approve","-lock=false"]
        self.terraform_refresh = ["terraform", "refresh", "-lock=false"]
        self.terraform_destroy = ["terraform", "destroy", "-auto-approve", "-lock=false"]

        self.terraform_workspace_new = ["terraform", "workspace", "new"]
        self.terraform_workspace_select = ["terraform", "workspace", "select"]
        self.terraform_workspace_select_default = ["terraform", "workspace", "select", "default"]
        self.terraform_workspace_delete = ["terraform", "workspace","delete"]
        self.deployment_configuration = ["terraform", "workspace","delete"]



def main():
    try:
        deployment_authentication = '-var-file=inputs/deployment/provider.json'
        p = executer()
        p.core()
        # executer.download_charts(self)
        # executer.core(self="namespace")
    except Exception as e:
        os.system("Error in execution" + e)


if __name__ == '__main__':
    main()
