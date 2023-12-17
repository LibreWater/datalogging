provider "grafana" {
  url = local.grafana_url
  #   auth = var.grafana_auth
}

terraform {
  required_providers {
    grafana = {
      source  = "grafana/grafana"
      version = ">= 2.8"
    }
  }
}
