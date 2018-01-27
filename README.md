# backend

## setup

```shell
# build docker image
docker build -t backend .

# run docker image in development mode
docker run --env-file .env --env FLASK_DEBUG=true --volume $PWD:/usr/src/app -p 80:5000 -it backend

# run docker image
docker run --env-file .env -p 80:5000 backend
```
