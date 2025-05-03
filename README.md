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