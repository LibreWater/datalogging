resource "grafana_organization" "this" {
  name = var.org_name
}

resource "grafana_folder" "this" {
  org_id = grafana_organization.this.org_id
  title  = var.folder_name
}

resource "grafana_dashboard" "this" {
  for_each    = toset(local.dashboard_files)
  org_id      = grafana_organization.this.org_id
  folder      = grafana_folder.this.id
  config_json = templatefile("${path.module}/dashboards/${each.value}", {})
}
