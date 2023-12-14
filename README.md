# Acraea data logging and visualisation

This setup is used to run Grafana and a TimescaleDB instance in docker containers

# Install

- Python
- pip install psycopg2
- Install Docker
- Clone repo locally

# Configuration

Depending on further 

# Docker Compose

- Navigate to cloned repo
- sudo docker-compose up -d
- python ./create_database.py
- Visit http://localhost:3000/ to view results in Grafana.

To exit use `sudo docker-compose down`

# Uninstall / reset

sudo docker-compose down
sudo docker rm -f datalogging_timescaledb_1
sudo docker rm -f datalogging_grafana_1
sudo docker volume rm datalogging_grafana-storage
sudo docker volume rm datalogging_timescaledb-data

## Dashboards

The docker-compose setup comes with two pre-built dashboards. One for listing the discrete test runs as a list, and the other for visualizing the results of a specific test run.

