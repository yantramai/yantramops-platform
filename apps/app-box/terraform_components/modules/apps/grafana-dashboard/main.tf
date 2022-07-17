/**
Base module for deploying helm charts.
**/
resource "grafana_dashboard" "metrics" {
  for_each = var.grafana_dashboards
  config_json =  file(each.value.grafana_dashboard_path)

}