
export REPO_ROOT=/home/rashmi/PycharmProjects/yantram_cloud/public_clouds

terraform destroy -var-file="$REPO_ROOT/google/gcp/ansible_components/resources/gcp_compute_facts.tfvars.json" -auto-approve
