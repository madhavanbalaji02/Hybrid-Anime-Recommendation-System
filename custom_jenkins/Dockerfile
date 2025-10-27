# Use Jenkins LTS on Debian Bullseye (stable base)
FROM jenkins/jenkins:lts-jdk17

USER root

# Install prerequisites and Docker CLI
RUN apt-get update -y && \
    apt-get install -y ca-certificates curl gnupg lsb-release && \
    mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
      https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
      > /etc/apt/sources.list.d/docker.list && \
    apt-get update -y && \
    apt-get install -y docker-ce-cli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add Jenkins user to Docker group
RUN groupadd -f docker && usermod -aG docker jenkins

# Prepare directory for Docker-in-Docker volume
RUN mkdir -p /var/lib/docker
VOLUME /var/lib/docker

USER jenkins
