/**
Base module for deploying civo clusters.
**/
resource "civo_kubernetes_cluster" "yantram-helm_release-stack" {
    api_endpoint = "my-cluster"
    name = "my-cluster"
    applications = "Portainer, Traefik"
    num_target_nodes = 4
    target_nodes_size = element(data.civo_instances_size.small.sizes, 0).name
}
