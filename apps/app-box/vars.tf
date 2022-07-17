# Input variable definitions

# kubernetes
variable "namespace" {default = "yantram"}
variable "kubernetes_configurations" { description = "MUST BE PASSED" }


# helm charts
variable "chart_configurations" {default = {} }

# grafana

variable "grafana_configurations" {default ={}}

variable "grafana_folders" { default ={} }
variable "grafana_data_sources" { default ={} }
variable "grafana_dashboards" { default ={} }
