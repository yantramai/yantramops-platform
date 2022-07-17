

//resource "civo_kubernetes_cluster" "my-cluster" {
//    api_endpoint = "my-cluster"
//    name = "my-cluster"
//    applications = "Portainer, Traefik"
//    num_target_nodes = 4
//    target_nodes_size = element(data.civo_instances_size.small.sizes, 0).name
//}

//provider "kubernetes" {
//  load_config_file = true
//  config_path="/home/rashmi/PycharmProjects/CloudDeployer/deployers/monitoring/apps/prometheus/mongodb/civo-yantram-kubeconfig"
////  host  = civo_kubernetes_cluster.my-cluster.api_endpoint
////  username = yamldecode(civo_kubernetes_cluster.my-cluster.kubeconfig).users[0].user.username
////  password = yamldecode(civo_kubernetes_cluster.my-cluster.kubeconfig).users[0].user.password
////  cluster_ca_certificate = base64decode(
////    yamldecode(civo_kubernetes_cluster.my-cluster.kubeconfig).clusters[0].cluster.certificate-authority-data
////  )
//}