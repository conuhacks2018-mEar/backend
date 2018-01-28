# backend

## setup

```shell
# build docker images
docker-compose build

# run docker containers
docker-compose up

# run on aws
docker-machine create --driver amazonec2 aws
eval $(docker-machine env aws)
docker-compose build
docker-compose up
```
