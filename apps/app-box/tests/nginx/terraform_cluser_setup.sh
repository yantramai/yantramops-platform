#!/bin/bash
#
# author: rashmi Kaushal
# site: http://yantram.cloud
# purpose: Basic kubectl introduction

+
~/tools/kind create cluster --name terraform-learn --config kind-config.yaml

mkdir learn-terraform-deploy-nginx-kubernetes
cd learn-terraform-deploy-nginx-kubernetes
kubectl config current-context