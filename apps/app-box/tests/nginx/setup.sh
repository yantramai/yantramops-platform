#!/bin/bash
#
# author: rashmi Kaushal
# site: http://yantram.cloud
# purpose: Basic kubectl introduction

curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.9.0/kind-linux-amd64
chmod +x ./kind
mv ./kind ~/tools/kind

curl https://raw.githubusercontent.com/hashicorp/learn-terraform-deploy-nginx-kubernetes-provider/master/kind-config.yaml --output kind-config.yaml


sudo docker login --username=jayantkaushal
sudo docker images
sudo docker tag 7ea1503bf816 jayantkaushal/yantram:firsttry
sudo docker push jayantkaushal/yantram:firsttry