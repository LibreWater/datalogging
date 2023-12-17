locals {
  dashboard_files = fileset("${path.module}/dashboards", "*.json")
}
