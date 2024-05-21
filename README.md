# Acraea data logging and visualisation

This setup can be used to run Grafana and a TimescaleDB instance in docker containers and a backend in django for the rest API.


## Install OS

Any Linux like system should work.


## Install the components (if not already present on the system)
The following has been tested on Ubuntu 22.04

### Python
```
sudo apt-get update
sudo apt-get install python3 #or whatever version you like
sudo apt install python3-pip
```

### Dependencies
```
sudo apt-get install libpq-dev
pip3 install psycopg2 django djangorestframework
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

#### Add the repository to Apt sources:
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

For Linux Mint:

```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$UBUNTU_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```


#### Install the Docker packages
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-compose
```

#### Verify that the Docker Engine installation is successful by running the hello-world image.
```
sudo docker run hello-world
```

### Clone repo locally
switch to desired location and type:
```
git clone https://github.com/LibreWater/datalogging.git
```
or
```
git clone git@github.com:LibreWater/datalogging.git
```


## Docker Compose

Navigate to cloned repo and stat the docker service. The first time it will download some files from the internet.


```
cd datalogging
sudo docker-compose up -d
```

Wait a bit, then visit http://localhost:3000/ to view results in Grafana.

To exit use:
```
sudo docker-compose down
```

## Start the backend server

```
cd backend
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
```


### configure UFW
If you use the firewall UFW, you can configure it to give the ESP32 access to the backend.
```
sudo ufw allow from 192.168.1.109 to any port 8000
```
assuming 192.168.1.109 is the IP address of the ESP32.

## Uninstall / reset
Warning: Deletes all data from Database

```
./reset_docker.sh
```
## Dashboards

The docker-compose setup comes with two pre-built dashboards. One for listing the discrete test runs as a list, and the other for visualizing the results of a specific test run.

