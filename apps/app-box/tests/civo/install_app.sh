kubectl config view
kubectl config set-context yantram-observer \
  --cluster=default \
  --namespace=yantram-observer \
  --user=default

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml



kubectl create deployment web --image=gcr.io/google-samples/hello-app:1.0
