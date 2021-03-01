#!/bin/bash
#
# author: Jayant Kaushal
# site: http://yantram.cloud
# purpose: Basic kubectl introduction

curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.9.0/kind-linux-amd64
chmod +x ./kind
mv ./kind ~/tools/kind

curl https://raw.githubusercontent.com/hashicorp/learn-terraform-deploy-nginx-kubernetes-provider/master/kind-config.yaml --output kind-config.yaml


