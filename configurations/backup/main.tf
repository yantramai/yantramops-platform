provider "kubernetes" {
  config_context_cluster = "minikube"
}
resource "kubernetes_namespace" "minikube-namespace" {
  metadata {
    name = "my-first-terraform-namespace"
  }
}
resource "kubernetes_deployment" "nginx" {
  metadata {
    name = "scalable-nginx-example"
    labels = {
      App = "ScalableNginxExample"
    }
  }

  spec {
    replicas = 2
    selector {
      match_labels = {
        App = "ScalableNginxExample"
      }
    }
    template {
      metadata {
        labels = {
          App = "ScalableNginxExample"
        }
      }
      spec {
        container {
          image = "nginx:1.7.8"
          name = "example"

          port {
            container_port = 80
          }

          resources {
            limits {
              cpu = "0.5"
              memory = "512Mi"
            }
            requests {
              cpu = "250m"
              memory = "50Mi"
            }
          }
        }
      }
    }
  }
}
resource "helm_release" "my_database" {
  name = "my-database"
  chart = "stable/mariadb"

  set {
    name = "mariadbUser"
    value = "foo"
  }

  set {
    name = "mariadbPassword"
    value = "qux"
  }
  set {
    type = "string"
    name = "image.tags"
    value = "registry\\.io/terraform-provider-helm\\,example\\.io/terraform-provider-helm"
  }
}



resource "helm_release" "helm_prometheus" {
  name = "prometheus-community-helm-example"
  repository = "https://prometheus-community.github.io/helm-charts"
  chart = "kube-prometheus-stack"

//  values = [
//    file("values.yaml")
//  ]

  set {
    name = "cluster.enabled"
    value = "true"
  }

  set {
    name = "metrics.enabled"
    value = "true"
  }
}
//resource "helm_release" "helm_awx" {
//  name = "helm_awx_example"
//  repository = "https://adwerx.github.io/charts"
//  chart = "adwerx"
//
////  values = [
////    file("values.yaml")
////  ]
//
//  set {
//    name = "cluster.enabled"
//    value = "true"
//  }
//
//  set {
//    name = "metrics.enabled"
//    value = "true"
//  }
//}


