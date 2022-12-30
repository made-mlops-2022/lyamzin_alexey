# Homework 2: Model Inference

## Geting Started locally

1. First pull this repository to your local computer
```
git pull git@github.com:made-mlops-2022/lyamzin_alexey.git
cd lyamzin_alexey
```
2. Get to the directory online_inference after checkout
```
git chekcout homework2
cd online_inference
```
3. Build an image with tag
```
docker build -t inference .
```
4. Run docker image
```
docker run -p 8000:8000 --name inference inference
```

## Getting Started with Docker Hub

1. First pull the corresponding docker-image from [Docker Hub](https://hub.docker.com/r/alexgrunt/mlops-made-service/tags)
```
docker pull alexgrunt/mlops-made-service:service
```

2. Start pulled container
```
docker run -p 8000:8000 --name inference alexgrunt/mlops-made-service:service
```

3. You are ready to go! Your service started at `localhost:8000`

4. Now you can run tests inside the running container using the following commands:
```
docker exec -it inference bash
python -m unittest
```
