provider "kubernetes" {
  config_context_cluster   = "minikube"
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
          name  = "example"

          port {
            container_port = 80
          }

          resources {
            limits {
              cpu    = "0.5"
              memory = "512Mi"
            }
            requests {
              cpu    = "250m"
              memory = "50Mi"
            }
          }
        }
      }
    }
  }
}
resource "helm_release" "example" {
  name       = "my-redis-release"
  repository = "https://kubernetes-charts.storage.googleapis.com"
  chart      = "redis"
  version    = "6.0.1"

  values = [
    file("values.yaml")
  ]

  set {
    name  = "cluster.enabled"
    value = "true"
  }

  set {
    name  = "metrics.enabled"
    value = "true"
  }

  set {
    type="string"
    name  = "service.annotations.prometheus\\.io/port"
    value = "9127"
  }
}



