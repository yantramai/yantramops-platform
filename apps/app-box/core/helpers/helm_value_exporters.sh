#!/bin/bash
#
# author: Jayant Kaushal
# site: http://yantram.cloud
# purpose: Basic kubectl introduction

helm ls
helm repo update

echo '#####################################################################################'
echo 'Listing all the Nodes'
echo '#####################################################################################'

helm show values bitnami/apache > yantram-apache.yaml
helm show values prometheus-community/prometheus-postgres-exporter > yantram-prometheus-postgres-exporter.yaml
helm show values prometheus-community/kube-prometheus-stack > yantram-kube-prometheus-stack.yaml

helm show values bitnami/mongodb > yantram-mongodb.yaml
helm show values prometheus-community/prometheus-mongodb-exporter > yantram-prometheus-mongodb-exporter.yaml


helm show values bitnami/mysql > yantram-mysql.yaml
helm show values prometheus-community/prometheus-mysql-exporter > yantram-prometheus-mysql-exporter.yaml
helm show values prometheus-community/prometheus-stackdriver-exporter > yantram-prometheus-stackdriver-exporter.yaml
helm repo add
helm show values cowboysysop/mongo-express > yantram-mongo-express.yaml


echo '#####################################################################################'


