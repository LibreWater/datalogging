# Acraea data logging and visualisation
This setup is used to run Grafana and a TimescaleDB instance in docker containers

# Install
- Install Docker
- Clone Repo locally

# Configuration
Depending on further 

# Docker Compose

- Navigate to cloned repo
- `docker-compose up -d` in terminal
- `python create_database.py`
- Visit http://localhost:3000/ to view results in Grafana.

## Dashboards

The docker-compose setup comes with two pre-built dashboards. One for listing the discrete test runs as a list, and the other for visualizing the results of a specific test run.

