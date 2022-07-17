
export REPO_ROOT=/home/rashmi/PycharmProjects/CloudDeployer/com/yantram/deployers/cloud/public_clouds

terraform init

terraform apply -var-file="$REPO_ROOT/google/gcp/ansible_components/resources/gcp_compute_facts.tfvars.json" -auto-approve

sh  $REPO_ROOT/google/gcp/ansible_components/provision_applications.sh