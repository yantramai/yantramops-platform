provider "helm" {
  kubernetes {
    config_path = var.kubernetes_configurations.config_path
    config_context = var.kubernetes_configurations.config_context_cluster
  }
}