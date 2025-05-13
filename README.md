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
    image: microhub-gateway:latest # Name and tag for the Docker image
    container_name: microhubgatewaycontainer # Custom name for the container
    ports:
      - "8000:8000" # Maps port 8000 on the host to port 8000 in the container. Here port map as <hostport>:<containerport>
    env_file: 
      - .env # Load all environment variables from the .env file
    environment:
      - DEBUG=$DEBUG
    volumes:
      - .:/microhub-gateway  # Bind-mounted local directory for live updates
    networks:
      - microhubnetwork # Connects to your custom network
    #restart: always # better for production. Automatically restarts the container if it stops or after a host machine reboot
    restart: unless-stopped # better for development. better for debuging. If you want to stop container manually then it will not again start automatically. It will start automatically when system reboot

networks:
  microhubnetwork:  # Ensure this name matches all other references
    driver: bridge
    name: microhub_network  # Explicitly name it

```

## How to manage `latest` and `version like 1.0,2.0, etc` tag of image
1. Always use the `latest` tag with image `docker-compose.yml` file in local machine
```
atul@atul-Lenovo-G570:~/microhub/microhub-gateway$ docker tag atulkrishnathakur/microhub-gateway:latest

```
2. Tag local machine `latest` for docker hub `latest`
```
atul@atul-Lenovo-G570:~/microhub/microhub-gateway$ docker tag microhub-gateway:latest atulkrishnathakur/microhub-gateway:latest

```
3. Delete latest tag image from docker hub before pushing `latest` tag image and push again
```
atul@atul-Lenovo-G570:~/microhub/microhub-gateway$ docker push atulkrishnathakur/microhub-gateway:latest

```

4. Tag image for version and push on docker hub
```
atul@atul-Lenovo-G570:~/microhub/microhub-gateway$ docker tag atulkrishnathakur/microhub-gateway:latest atulkrishnathakur/microhub-gateway:1.0

```

## how to use httpx
1. Reference: https://www.python-httpx.org


## How to send post request from gateway to service using httpx 
- create the `app/main.py` file
```
from fastapi import FastAPI
from pydantic import (BaseModel,Field, model_validator, EmailStr, ModelWrapValidatorHandler, ValidationError, AfterValidator,BeforeValidator,PlainValidator, ValidatorFunctionWrapHandler)
from typing import List
import httpx

app = FastAPI()
    
@app.post("/mytest")
async def test():
    async with httpx.AsyncClient() as client:
        try:
            res = await client.post('http://microhubusermanagementcontainer:8000/a1', json={"abc":123},headers={"Content-Type": "application/json"}, timeout=None)
            res.raise_for_status()  # HTTP error raise karega agar status code 4xx/5xx ho
            return res.json()
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")



class EmpSchemaIn(BaseModel):
    emp_name: str = Field(example="Atul")
    email: EmailStr = Field(example="atul@comsysapp.com")
    mobile: str | None = Field(example="000000")
    status: int | None = Field(default=1)
    password: str = Field(example="aa")
    confirm_password:str = Field(example="aa")
    
@app.post("/mytest2")
async def mytest2(empm: EmpSchemaIn):
    async with httpx.AsyncClient() as client:
        try:
            res = await client.post('http://microhubusermanagementcontainer:8000/a2',json={"empm":empm.dict()},headers={"Content-Type": "application/json"}, timeout=None)
            res.raise_for_status()  # HTTP error raise karega agar status code 4xx/5xx ho
            return res.json()
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")


```



