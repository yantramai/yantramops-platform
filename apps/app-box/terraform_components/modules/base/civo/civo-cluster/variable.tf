# Input variable definitions
variable "namespace" {
  description = "Namespace"
  type = string
}
variable "civo_clusrer_configurations" {
  description = "helm configurations to be deployed in the cluster"
  type = map(map(string))
  default = {}
}