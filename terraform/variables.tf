variable "grafana_sslmode" {
  type    = string
  default = "require"
}

variable "grafana_port" {
  type    = number
  default = 3000
}

variable "grafana_host" {
  type    = string
  default = "localhost"
}
