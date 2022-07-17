kubectl port-forward services/yantram-kube-prometheus-st-prometheus 9090 --namespace=yantram
kubectl port-forward services/yantram-loki-stack  3100 --namespace=yantram
kubectl port-forward services/yantram-prometheus-mongodb-exporter  9216 --namespace=yantram
kubectl port-forward services/prometheus-postgres-exporter 9187:80 --namespace=yantram
kubectl port-forward services/yantram-postgresql 5432:80 --namespace=yantram
kubectl port-forward services/yantram-apachel 7777:80 --namespace=yantram
kubectl port-forward services/yantram-apache-exporter 9117 --namespace=yantram

# kubectl describe servicemonitor prometheus-mongodb-exporter
kubectl describe servicemonitor prometheus-postgres-exporter

kubectl expose deployment web --type=NodePort --port=8080

kubectl exec --namespace=yantram --stdin --tty yantram-postgresql-postgresql-0 -- /bin/bash


yantram-kube-prometheus-stack-grafana
# kubectl port-forward services/yantram-prometheus-kube-pr-prometheus 9090
kubectl port-forward services/yantram-kube-prometheus-st-prometheus 9090
kubectl port-forward services/yantram-postgresql 9090
kubectl port-forward services/yantram-kube-prometheus-stack-grafana 3000:80
kubectl port-forward services/prometheus-mongodb-exporter 9216 --namespace=yantram
kubectl port-forward services/prometheus-postgres-exporter 5555:80
# kubectl port-forward services/yantram-prometheus-prometheus-node-exporter 9100
kubectl port-forward services/yantram-kube-prometheus-stack-grafana 3000:80 --namespace=yantram
kubectl port-forward services/yantram-mongodb 27017 --namespace=yantram
kubectl port-forward services/yantram-mongo-express 8081 --namespace=yantram


prometheus-postgres-exporter
# helm show values prometheus-community/prometheus-postgres-exporter > yantram-postgres-exporter.yaml
prometheus-mongodb-exporter
curl -g 'http://localhost:9090/api/v1/series?' \
    --data-urlencode 'match[]=up' --data-urlencode 'match[]=process_start_time_seconds{job="prometheus"}'
curl -g 'http://localhost:9090/api/v1/labels?' --data-urlencode 'match[]=up' --data-urlencode 'match[]=process_start_time_seconds{job="prometheus"}'
curl 'http://localhost:9090/api/v1/query_range?query=up&start=2015-07-01T20:10:30.781Z&end=2015-07-01T20:11:00.781Z&step=15s'
curl -G http://localhost:9091/api/v1/targets/metadata \
    --data-urlencode 'match_target={instance="127.0.0.1:9090"}'

curl http://localhost:9090/api/v1/alertmanagers

curl 'http://localhost:9090/api/v1/query_range?query=up&start=2015-07-01T20:10:30.781Z&end=2015-07-01T20:11:00.781Z&step=15s'
curl -g 'http://localhost:9090/api/v1/series?' --data-urlencode 'match[]=up' --data-urlencode 'match[]=process_start_time_seconds{job="prometheus"}'
