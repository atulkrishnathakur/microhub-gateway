## start gateway
```
atul@atul-Lenovo-G570:~$ cd microhub/microhub-gateway
atul@atul-Lenovo-G570:~/microhub/microhub-gateway$ git init
atul@atul-Lenovo-G570:~/microhub/microhub-gateway$ git config user.name "A**l"
atul@atul-Lenovo-G570:~/microhub/microhub-gateway$ git config user.email "d****@***.com"
atul@atul-Lenovo-G570:~/microhub/microhub-gateway$ git remote add origin https://github.com/username/microhub-gateway.git
atul@atul-Lenovo-G570:~/microhub/microhub-gateway$ git remote -v
origin	https://github.com/username/microhub-gateway.git (fetch)
origin	https://github.com/username/microhub-gateway.git (push)
atul@atul-Lenovo-G570:~/microhub/microhub-gateway$ 
```

## create image and run using docker compose

```
atul@atul-Lenovo-G570:~/microhub/microhub-gateway$ docker compose up -d --build
```

## Now check in browser
```
http://localhost:8000/docs
```

## About network
1. define network in gateway `docker-compose.yml` file because gateway is the entry point of microservices.
```
# version: '3.9' # Defines the version of Docker Compose being used. No need to write in newer version in docker compose file
services:
  microhub-gateway: # Service for your FastAPI application
    build:
      context: . # Directory containing the Dockerfile
      dockerfile: Dockerfile # Path to the Dockerfile for building the image
    image: microhub-gateway:1.0 # Name and tag for the Docker image
    container_name: microhubgatewaycontainer # Custom name for the container
    ports:
      - "8000:8000" # Maps port 8000 on the host to port 8000 in the container. Here port map as <hostport>:<containerport>
    networks:
      - microhubnetwork # Connects to your custom network
    restart: always # Automatically restarts the container if it stops or after a host machine reboot

networks:
  microhubnetwork:  # Ensure this name matches all other references
    driver: bridge
    name: microhub_network  # Explicitly name it
```