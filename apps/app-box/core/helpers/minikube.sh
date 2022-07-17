#minukube should be running, if not uncomment below.
docker info --format '{{.OSType}}'

echo ----------------------------------------------------- Deleting Minikube Cluster------------------------------------------

minikube delete

minikube start --kubernetes-version=v1.19.0 --memory=4096
minikube addons disable metrics-server
# minikube addons enable ingress

sh terraform.sh base
sh terraform.sh application
sh terraform.sh mongo
sh terraform.sh postgres
#

kubectl delete -f yantram-apache-exporter.yaml -n yantram
#
#minikube start --kubernetes-version=v1.19.0 --memory=8192 --extra-config=kubelet.authentication-token-webhook=true --extra-config=kubelet.authorization-mode=Webhook --extra-config=scheduler.address=0.0.0.0 --extra-config=controller-manager.address=0.0.0.0
#minikube start --kubernetes-version=v1.11.1 --memory=8192 --bootstrapper=kubeadm --extra-config=kubelet.authentication-token-webhook=true --extra-config=kubelet.authorization-mode=Webhook --extra-config=scheduler.address=0.0.0.0 --extra-config=controller-manager.address=0.0.0.0

#terraform init


#terraform apply -auto-approve


# sh kubectl.sh

#terraform apply -var-file="$REPO_ROOT/google/gcp/ansible_components/resources/gcp_compute_facts.tfvars.json" -auto-approve
#terraform apply -auto-approve
#
#
#sh  $REPO_ROOT/google/gcp/ansible_components/provision_applications.sh

# Expose Prometheus UI after installing prometheus-community-chart
#
#
# NAMESPACE="default" /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/grafana/agent/v0.12.0/production/kubernetes/install.sh)" | kubectl apply -f -
# NAMESPACE="default" /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/grafana/agent/v0.12.0/production/kubernetes/install-loki.sh)" | kubectl apply -f -
# NAMESPACE="default" /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/grafana/agent/v0.12.0/production/kubernetes/install-tempo.sh)" | kubectl apply -f -


kubectl delete crd -n core alertmanagers.monitoring.coreos.com --namespace=yantram
kubectl delete crd -n core podmonitors.monitoring.coreos.com --namespace=yantram
kubectl delete crd -n core prometheuses.monitoring.coreos.com --namespace=yantram
kubectl delete crd -n core prometheusrules.monitoring.coreos.com --namespace=yantram
kubectl delete crd -n core servicemonitors.monitoring.coreos.com --namespace=yantram
kubectl delete crd -n core thanosrulers.monitoring.coreos.com --namespace=yantram
