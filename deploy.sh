#!/bin/bash

# Deployment script for datetime MCP server

# Set variables
IMAGE_NAME="datetime-mcp"
TAG="latest"
CONTAINER_NAME="datetime-mcp-server"
PORT=8000

echo "Building Docker image..."
docker build -t $IMAGE_NAME:$TAG .

if [ $? -eq 0 ]; then
    echo "SUCCESS: Docker image built successfully!"
    
    echo "Stopping existing container (if any)..."
    docker stop $CONTAINER_NAME 2>/dev/null || true
    docker rm $CONTAINER_NAME 2>/dev/null || true
    
    echo "Starting new container..."
    docker run -d \
        --name $CONTAINER_NAME \
        -p $PORT:8000 \
        --restart unless-stopped \
        $IMAGE_NAME:$TAG
    
    if [ $? -eq 0 ]; then
        echo "SUCCESS: Container started successfully!"
        echo "Server is running at: http://localhost:$PORT"
        echo "Health check: http://localhost:$PORT/health"
        echo ""
        echo "To view logs: docker logs $CONTAINER_NAME"
        echo "To stop: docker stop $CONTAINER_NAME"
    else
        echo "ERROR: Failed to start container"
        exit 1
    fi
else
    echo "ERROR: Failed to build Docker image"
    exit 1
fi 