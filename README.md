# Acraea data logging and visualisation

This setup is used to run Grafana and a TimescaleDB instance in docker containers

## Install the components (if not already present on the system)
The following has been tested on Ubuntu 22.04

### Python
```
sudo apt-get update
sudo apt-get install python3 #or whatever version you like
```

### Dependency for database creation
```
pip3 install psycopg2
```

### Install Docker

#### Add Docker's official GPG key:
```
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

##### Add the repository to Apt sources:
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

#### Install the Docker packages
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

#### Verify that the Docker Engine installation is successful by running the hello-world image.
```
sudo docker run hello-world
```

### Clone repo locally
switch to desired location and type:
```
git clone git@github.com:LibreWater/datalogging.git
```

## Configuration

Depending on future sensor readings we'd need to update the database creation script (create_database.py)

## Docker Compose

Navigate to cloned repo

```
sudo docker-compose up -d
python ./create_database.py
```

Visit http://localhost:3000/ to view results in Grafana.

To exit use:
```
sudo docker-compose down
```

## Uninstall / reset
```
./reset_docker.sh
```
## Dashboards

The docker-compose setup comes with two pre-built dashboards. One for listing the discrete test runs as a list, and the other for visualizing the results of a specific test run.

