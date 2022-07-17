/**
Base module for deploying helm charts.
**/
resource "grafana_data_source" "yantram-grafana_data_source" {
  for_each = var.grafana_data_sources
  name = each.value.name
  type = each.value.type
  username = each.value.username
  password = each.value.password
  url = each.value.url
}