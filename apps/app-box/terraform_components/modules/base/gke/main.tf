# main.tf
terraform {
  backend "remote" {
    organization = "hashicorp-learn"

    workspaces {
      name = "learn-terraform-pipelines-k8s"
    }
  }
}