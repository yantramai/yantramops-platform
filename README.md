# README #

### About : 
* A Terraform and Helm based kubernetes application deployment engine.
* Special focus on building prometheus application monitoring deploynments and their grafana dashboards and other components.
* Lets you run and manage a set of applications in a kubernetes namesapce as virtual containers. 


### An example deployment for prometheus. 
lets just directly look at one deployment which as an app component developer is all what you will need.
  * workspace: a virtual container with its own lifecycle.
  * lifecycle_event: 4 life cycle events are supported for this virtual container.
      * create
      * refresh
      * skip
      * destroy
  * deployment_configurations : you can define individual components to be deployed in each of this virtual container.
      * deployments/kube.json
      * deployments/postgresql.json
      * deployments/postgresql.json
  more on the structure of these deployment configurations in next section.
```
# deployment.yaml 
---
namespace: yantram
deployments:
- workspace: kube-prometheus-stack
  lifecycle_event: create
  deployment_configurations:
    - deployments/kube.json
- workspace: postgresql
  lifecycle_event: create
  deployment_configurations:
    - deployments/postgresql.json
- workspace: mongodb
  lifecycle_event: refresh
  deployment_configurations:
    - deployments/mongo.json
- workspace: mongo-express
  lifecycle_event: destroy
  deployment_configurations:
    - deployments/mongo_express.json
- workspace: apache
  provider_configuration: deployments/provider.json
  lifecycle_event: skip
  deployment_configurations:
    - deployments/apache.json
```

### Deployment Configurations 
Following are the components of your deployment configurations.
  * namespace: a kubernetes namespace for deployments and services to be created.
  * chart_configurations: helm charts to be deployed as part of this deployment.
     * name: Name of the chart 
     * chart: chart name as specified in the charts.yaml 
     * chart_values: Input values to be defined for each chart. upon every chart installation default values of this chart will be downloaded into input/default_chart_values   
     * repository: repository name 
     * create_namespace: create kubernetes namespace as part of this deployment. 
```
{
  "namespace": "yantram",
  "chart_configurations": {
    "kube-prometheus-stack": {
      "name": "kube-prometheus-stack",
      "chart": "kube-prometheus-stack",
      "chart_values": "inputs/app/yantram-kube-prometheus-stack.yaml",
      "repository": "https://prometheus-community.github.io/helm-charts",
      "create_namespace": true
    },
    "postgresql": {
      "name": "postgresql",
      "chart": "postgresql",
      "chart_values": "inputs/app/yantram-postgresql.yaml",
      "repository": "https://charts.bitnami.com/bitnami",
      "create_namespace": false
    },
    "prometheus-postgres-exporter": {
      "name": "prometheus-postgres-exporter",
      "chart": "prometheus-postgres-exporter",
      "chart_values": "inputs/exporters/yantram-prometheus-postgres-exporter.yaml",
      "repository": "https://prometheus-community.github.io/helm-charts",
      "create_namespace": false
    }
  },
  "grafana_folders": {
    "grafana_dashboard_folder": {
      "grafana_dashboard_folder": "yantram"
    }
  },
  "grafana_data_sources": {
    "postgresql": {
      "name": "postgresql",
      "type": "postgres",
      "url": "yantram-postgresql:5432",
      "username": "postgres",
      "password": "postgres",
      "database": "postgres"
    }
  },
  "grafana_dashboards": {
    "postgresql_dashboard": {
      "grafana_dashboard_path": "inputs/dashboards/9106-postgresql_rev1.json"
    }
  }
}
```

### Dependencies:
   * Terraform v0.12.18 [Terraform Setup](https://learn.hashicorp.com/tutorials/terraform/install-cli)
   * Helm v3.3.4 [Helm Setup](https://helm.sh/docs/intro/install/)
   * git 2.27.0
   * kubectl 2.27.0

### Setup: 
  * Installation :
```
kubectl apply -f  deployments.yaml
```

### Run: 
```
python3 execute.py
```

### Further development ###

TBD

### Known bugs ###

TBD.

### Who do I talk to? ###

* Repo owner or admin
* jayant@yantram.cloud