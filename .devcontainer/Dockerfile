# Use the official image as a parent image
FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Set the working directory
WORKDIR /workspace

# Install fontconfig
RUN apt-get update && apt-get install -y fontconfig

# Copy the rest of the application code
COPY . .
