#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Jayant Kaushal <jayant@yantram.cloud>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import json
import yaml
from apps.core.processor.yantram_processor import YantramProcessor as yantram


class YantramExecuter:

    def download_charts(self):
        yantram.download_charts(self=self, deployment_file='../../app-box/deployments.yaml')

    def core(self):
        yantram.invoke_process(yantram.terraform_init)
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
