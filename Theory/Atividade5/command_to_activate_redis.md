# How to use Redis

## Pull the image with docker

```bash
docker pull redis
```

## Executing container

```bash
docker run -d --name redis-container -p 6379:6379 redis
```

## Verifing if the container was created

```bash
docker container ps
```

## Looking the container

```bash
docker exec -it redis-container redis-cli
```