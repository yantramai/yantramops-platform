/**
Base module for deploying helm charts.
**/


// Terraform plugin for creating random ids
//resource "google_compute_network" "default_network" {
//  for_each = var.gcp_inputs
//  name = format("%s-%s",  each.value.client, each.value.client)
//}

resource "google_compute_firewall" "default_firewall" {
  for_each = var.gcp_inputs
  name = format("%s-%s-%s",  each.value.client,"firewall", each.value.name)
  network = "google_compute_network.default_network.name"
//  network = google_compute_network.default_network.name
  allow {
    protocol = "icmp"
  }
  allow {
    protocol = "tcp"
    ports = [
      "22",
      "80",
      "8080",
      "1000-2000"]
  }
//  source_tags = var.server_tags
}
// A single Compute Engine instance
resource "google_compute_instance" "default_instance" {
  for_each = var.gcp_inputs
  name = format("%s-%s-%s",  each.value.client,"instance", each.value.name)
  tags = each.value.server_tags
  machine_type = each.value.machine_type
  zone = each.value.zone
  boot_disk {
    initialize_params {
      image = each.value.source_image
    }
  }
  // Make sure flask is installed on all new instances for later steps
//  metadata_startup_script = "sudo apt-get update; sudo apt-get install -yq build-essential python-pip rsync; pip install flask"
  metadata = {
    ssh-keys = "yantram:${file(each.value.public_key_file)}"
  }
  network_interface {
//    network = google_compute_network.default_network.name
    access_config {
      // Include this section to give the VM an external ip address
    }
  }
}