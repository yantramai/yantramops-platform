/**
Base module for deploying helm charts.
**/
resource "helm_release" "yantram1-helm_release-stack" {
  for_each = var.helm_chart_list
  name = format("%s-%s",  var.namespace, each.value.name)
  repository = each.value.repository
  chart = each.value.chart
  values = [
    file(each.value.chart_values)
  ]
  recreate_pods = false
  cleanup_on_fail = false
  namespace = var.namespace
  create_namespace = each.value.create_namespace != "" ? each.value.create_namespace : false
}
