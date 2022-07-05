FROM python:3.9.1
LABEL maintainer="jayant_kaushal@yahoo.com"
RUN apt-get update && \
    mkdir -p /kubernetes-app-engine
COPY ../kubernetes-app-engine /kubernetes-app-engine
WORKDIR /kubernetes-app-engine
RUN python3 -m pip install --upgrade pip && \
    pip3 install -r requirements.txt && \