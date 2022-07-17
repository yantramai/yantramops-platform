#!/bin/bash



#terraform apply -var-file="$REPO_ROOT/google/gcp/ansible_components/resources/gcp_compute_facts.tfvars.json" -auto-approve
terraform destroy -auto-approve
#
#
#sh  $REPO_ROOT/google/gcp/ansible_components/provision_applications.sh
