FROM ubuntu
LABEL maintainer="jayant_kaushal@yahoo.com"
RUN apt-get update && mkdir -p /kubernetes-app-engine
RUN add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main"
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add -
RUN apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" -y
RUN apt-get update
RUN apt-get -y install kubectl terraform
RUN python3 -m pip install --upgrade pip && \
    pip3 install -r requirements.txt && \
