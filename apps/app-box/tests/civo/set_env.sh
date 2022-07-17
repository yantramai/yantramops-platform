# open .bashrc
# append below export command at the very end.
terraform workspace new yantram

kubectl config unset contexts.default
kubectl config delete-context default

#
export KUBECONFIG=/home/rashmi/PycharmProjects/CloudDeployer/com/yantram/deployers/containers/kubernates/civo/config/civo-yantram-k8-kubeconfig
export KUBECONFIG=~/.kube/config

# # run source .bashrc

kubectl config set-context default \
  --cluster=default \
  --namespace=default \
  --user=default
echo $KUBECONFIG
kubectl config view

kubectl config view
kubectl config use-context default
kubectl get node

# kubectl config set-context yantram-observer \
#   --cluster=default \
#   --namespace=yantram-observer \
#   --user=default
# #
# # echo 'Use default the config'
# #
# kubectl config use-context yantram-observer


# kubectl config set-context default \
#   --cluster=default \
#   --user=default
#
# kubectl config use-context default
