# FastAPI Docker App

This is a simple FastAPI app that demonstrates how to use Docker to deploy a FastAPI app.

## Prerequisites

- Docker
- Python 3.11

## Usage

1. Clone the repository:

```bash
git clone https://github.com/pauldj/fastapi-docker-app.git
```

2. Navigate to the project directory:

```bash
cd fastapi-docker-app
```

3. Build the Docker image:

```bash
docker build -t fastapi-app .
# for multi-arch builds
docker buildx build --platform linux/amd64,linux/arm64 -t fastapi-app .
docker buildx build --platform linux/amd64,linux/arm64 -t <your-registry>/fastapi-docker-app:latest --push .
docker buildx build --platform linux/amd64,linux/arm64 -t ghcr.io/pauldjmetsi/fastapi-docker-app:latest --push .

# login to ghcr.io
echo $GITHUB_TOKEN | docker login ghcr.io -u <username> --password-stdin

# inspect the image
docker buildx imagetools inspect ghcr.io/<user>/fastapi-demo:latest
```

4. Run the Docker container:

```bash
docker run -p 8080:8080 fastapi-app

docker run -p 8080:8080 \
  -e APP_ENV=dev \
  -e APP_NAME=my-app \
  -e FEATURE_FLAG=true \
  -e API_KEY=supersecret \
  fastapi-demo
```

5. Access the app at: 
```
# Root 
http://localhost:8080/

# Config
http://localhost:8080/config

# Secure Endpoint
http://localhost:8080/secure?key=supersecret
```

## Configuration

The app can be configured using environment variables.  

| Variable | Description | Default Value |      
|----------|-------------|---------------|
| APP_ENV  | The app environment (dev, prod, etc.) | dev |
| APP_NAME | The name of the app | fastapi-demo |
| FEATURE_FLAG | Enable or disable a feature | false |
| API_KEY | The API key for secure endpoints | defaultkey |

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.   

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)  
- [Docker](https://www.docker.com/)  
- [Python](https://www.python.org/)     