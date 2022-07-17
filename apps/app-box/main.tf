module "helm_chart" {
  source = "terraform_components\/modules\/apps\/yantram-helm_chart-component"
  namespace = var.namespace
  helm_chart_list = var.chart_configurations
}