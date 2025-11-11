# DevEnv-Buddy: Docker Compose Lab 

**Lab Completed:** 2025-11-11 15:55:00

This lab demonstrates a functional multi-container development environment using Docker Compose. It includes:

- A custom Python web app (`devenvbuddy/main.py`)
- MySQL container with environment setup
- Healthcheck for web service

---

## Project Structure

```
DevEnv-Buddy/
├── devenvbuddy/
│   ├── main.py
│   └── __init__.py
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── logs/
├── tests/
└── README.md
```

---

## Dockerfile

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "devenvbuddy/main.py"]
```

---

## docker-compose.yaml

```yaml
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8080:8080"
    depends_on:
      - db
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080"]
      interval: 30s
      timeout: 10s
      retries: 3

  db:
    image: mysql:8
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: root
```

---

##  Run the Project

```bash
# Inside DevEnv-Buddy/
docker compose up --build -d

# Check containers
docker ps

# View logs
docker logs -f devenv-buddy-web-1
```

Visit in browser: [http://localhost:8080](http://localhost:8080)

---

## Troubleshooting

```bash
# Clean up networks if ports are stuck
docker network prune

# Shut everything down
docker compose down
```

---

## Logging Output

```bash
docker ps > logs/container_status.txt
docker logs devenv-buddy-web-1 > logs/web_output.txt
docker logs devenv-buddy-db-1 > logs/mysql_output.txt
```

---

## Git Commands

```bash
git add .
git commit -m "Lab complete: Working 3-container DevEnv-Buddy stack"
git push
```

---

**Author:** Jason Dickey  
**Date:** November 11, 2025
