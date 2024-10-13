# author: rashmi Kaushal
# site: http://yantram.cloud
# purpose: Basic kubectl introduction

#!/bin/bash
#
echo $1

echo '\n'
echo 'Debug a kubernetes pod -- log in to application terminal and then look inside \n'

kubectl get servicemonitor yantram-kube-prometheus-st-grafana --namespace=$1 -o yaml > ../sample/base/prometheus-mongodb-exporter-service-monitor.yml
kubectl get servicemonitor yantram-prometheus-postgres-exporter --namespace=yantram -o yaml > ../sample/base/yantram-prometheus-postgres-exporter-service-monitor.yml
kubectl get servicemonitor prometheus-mongodb-exporter -o yaml > ../sample/service/mongo/prometheus-mongodb-exporter-service-monitor.yml

# kubectl logs mysql-1600416151-689d49c5fb-wzh4h --namespace=$1


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


