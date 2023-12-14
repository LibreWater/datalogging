#!/bin/bash
sudo docker-compose down
sudo docker rm -f datalogging_timescaledb_1
sudo docker rm -f datalogging_grafana_1
sudo docker volume rm datalogging_grafana-storage
sudo docker volume rm datalogging_timescaledb-data
