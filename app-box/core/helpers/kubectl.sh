#!/bin/bash
#
echo $1
# author: Jayant Kaushal
# site: http://yantram.cloud
# purpose: Basic kubectl introduction

#list all the nodes running. remember if you are running minicube, there will be only one node which will act both and master and worker node
#echo 'Get Help on kubectl \n'
#kubectl -h
# kubectl config view
#
# # kubectl config set-context yantram-observer \
# #   --cluster=default \
# #   --namespace=yantram-observer \
# #   --user=default
# # #
# # # echo 'Use default the config'
# # #
# kubectl config use-context default
# # kubectl config use-context yantram-observer
#
#
# # kubectl config set-context default \
# #   --cluster=default \
# #   --user=default
# #
kubectl get namespace

echo '#####################################################################################'
echo 'Listing all the Nodes'
echo '#####################################################################################'
kubectl get nodes --namespace=$1
echo '#####################################################################################'

#get pods
#echo '\n'
#echo 'Describing node minicube \n'

#kubectl describe node minikube
#kubectl delete node mysql-1601062233-f675f9c4-59nww


#minikube start
#get pods
echo 'services'
echo '#####################################################################################'
kubectl get services --namespace=$1
echo '#####################################################################################'
echo 'servicemonitor'
kubectl get servicemonitor --namespace=$1
echo '#####################################################################################'
echo 'pods'
echo '#####################################################################################'
kubectl get pods --namespace=$1
echo '#####################################################################################'
echo 'deployments'
echo '#####################################################################################'
kubectl get deployment --namespace=$1
echo '#####################################################################################'
echo ' replicaset' --namespace=$1
echo '#####################################################################################'
kubectl get replicaset --namespace=$1
echo '#####################################################################################'
echo 'statefulset'
echo '#####################################################################################'
kubectl get statefulset --namespace=$1
echo '#####################################################################################'
echo 'configmap'
echo '#####################################################################################'
kubectl get configmap --namespace=$1
echo '#####################################################################################'
echo 'secret'
echo '#####################################################################################'
kubectl get secret --namespace=$1
#echo 'Edit a deployment : #kubectl edit DEPLOYMENT_NAME\n'
##kubectl edit deployment mysql-1600416151
#echo 'installed_helm_charts'
echo '#####################################################################################'
echo 'endpoints'
echo '#####################################################################################'

kubectl get endpoints --namespace=$1
echo '#####################################################################################'
echo 'crd'
echo '#####################################################################################'
kubectl get crd --namespace=$1
echo '#####################################################################################'
echo 'alertmanager'
echo '#####################################################################################'
kubectl get alertmanager --namespace=$1
echo '#####################################################################################'
echo 'prometheus'
echo '#####################################################################################'
kubectl get prometheus --namespace=$1
echo '#####################################################################################'
echo 'prometheusrules'
echo '#####################################################################################'
kubectl get prometheusrules --namespace=$1
echo '#####################################################################################'
echo 'alertmanagerconfigs'
echo '#####################################################################################'
kubectl get alertmanagerconfigs --namespace=$1
echo '#####################################################################################'


#helm ls
#helm repo update
#echo '\n'
#echo 'Debug a kubernetes pod -- log in to application terminal and then look inside \n'
#kubectl logs mysql-1600416151-689d49c5fb-wzh4h
#helm show values prometheus-community/prometheus-postgres-exporter > yantram-postgresql-exporter.yaml

# kubectl get configmap prometheus-postgres-exporter -o yaml > ../sample/configmap/prometheus-postgres-exporter.yml
# kubectl get configmap yantram-prometheus-grafana -o yaml > ../sample/configmap/yantram-prometheus-grafana.yml
#
# kubectl get services yantram-postgresql -o yaml > ../sample/service/yantram-postgresql.yml --namespace=$1
# kubectl get services yantram-postgresql-postgresql-0 -o yaml > ../sample/service/yantram-postgresql.yml --namespace=$1
# kubectl get services yantram-postgresql -o yaml --namespace=$1
# kubectl get deployments yantram-mongodb -o yaml > ../sample/service/yantram-mongodb.yml
# kubectl get crd prometheuses.monitoring.coreos.com -o yaml > ../sample/service/yantram-prometheuses.yml --
# kubectl get crd probes.monitoring.coreos.com -o yaml > ../sample/service/yantram-probes.yml
#
#
# kubectl get service prometheus-mongodb-exporter -o yaml > ../sample/service/mongo/prometheus-mongodb-exporter-service.yml
# kubectl get servicemonitor prometheus-mongodb-exporter -o yaml > ../sample/service/mongo/prometheus-mongodb-exporter-service-monitor.yml
# kubectl get pod prometheus-mongodb-exporter-7ffbbbc4b9-8xn27 -o yaml > ../sample/service/mongo/prometheus-mongodb-exporter-pod-7ffbbbc4b9-8xn27.yml
# kubectl get deployment prometheus-mongodb-exporter -o yaml > ../sample/service/mongo/prometheus-mongodb-exporter-dep.yml
#
#
#
# kubectl get pod yantram-prometheus-kube-pr-operator-5dfd84b9b7-5rtxm -o yaml > ../sample/service/prom_operator/yantram-prometheus-kube-pr-operator-5dfd84b9b7-5rtxm-pod-7ffbbbc4b9-8xn27.yml
# kubectl get deployment yantram-prometheus-kube-pr-operator -o yaml > ../sample/service/prom_operator/yantram-prometheus-kube-pr-operator-dep.yml
# kubectl get service yantram-prometheus-kube-pr-operator -o yaml > ../sample/service/prom_operator/yantram-prometheus-kube-pr-operator-service.yml
# kubectl get servicemonitor yantram-prometheus-kube-pr-operator -o yaml > ../sample/service/prom_operator/yantram-prometheus-kube-pr-operator-service-monitor.yml

#echo '\n'
#echo 'Describe a kubernetes pod -- remember it takes a pod to debug , not deployment, not service not anything else \n'
##kubectl describe pod mysql-1600416151-689d49c5fb-wzh4h
#echo 'Debug a kubernetes pod -- remember it takes a pod to debug , not deployment, not service not anything else \n'
##kubectl exec -it echo '\n'
#echo 'Debug a kubernetes pod -- remember it takes a pod to debug , not deployment, not service not anything else \n'
#kubectl exec  mysql-1600416151-689d49c5fb-wzh4h -- bin/bash -it
#
#kubectl get configmap prometheus-prometheus-operator-160106-prometheus-rulefiles-0 -o yaml > configmap/config.yml
#kubectl get configmap prometheus-postgres-exporter -o yaml > configmap/prometheus-postgres-exporter.yml
#
#echo 'Delete a deployment \n'
##kubectl delete deployment  mysql-1600416151



# kubectl config --kubeconfig=civo-yantram-k8-kubeconfig view
# kubectl config --kubeconfig=civo-yantram-k8-kubeconfig use-context default


