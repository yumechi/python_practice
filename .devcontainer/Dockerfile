# Use mcr.microsoft.com/devcontainers/python:3.12 as the base image
FROM mcr.microsoft.com/devcontainers/python:3.12

# Install mise system-wide
RUN curl https://mise.run | sh && \
    cp /root/.local/bin/mise /usr/local/bin/ && \
    chmod +x /usr/local/bin/mise
