# Input variable definitions
variable "namespace" {
  description = "Namespace"
  type = string
}
variable "helm_chart_list" {
  description = "helm configurations to be deployed in the cluster"
  type = map(map(string))
  default = {}
}