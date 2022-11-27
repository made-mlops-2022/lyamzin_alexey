# Homework 2: Model Inference

## Getting Started

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