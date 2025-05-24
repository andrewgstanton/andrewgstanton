#!/bin/bash

IMAGE_NAME=generate-profile
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"	
	
cd "$ROOT_DIR"

# 1. Build image if it doesn't exist
if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" == "" ]]; then
    echo "Building Docker image: $IMAGE_NAME"
    docker build -t $IMAGE_NAME .
fi

# 2. Run with current project directory mounted into /app
docker run --rm -v "$PWD":/app $IMAGE_NAME scripts/generate_profile.py

