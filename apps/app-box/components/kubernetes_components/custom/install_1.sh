install.sh
kubectl  delete deployment yantram-app-engine
kubectl  delete configmap setup-script
kubectl apply -f deployment.yaml

kubectl get pod

kubectl exec --stdin --tty yantram-app-engine-65ddc49c67-bwmzm  -- /bin/bash
kubectl logs yantram-app-engine-6466cdbd5d-kvhft --follow

apt-get update -y
apt-get install -y gnupg2 software-properties-common curl apt-transport-https gnupg2 curl git

curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list
apt-get update && apt-get install -y kubectl

curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add -
apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" -y
apt-get update  -y && apt-get install -y terraform

mkdir -p
git clone https://github.com/yantramcloud/kubernetes-app-engine /setup-script
