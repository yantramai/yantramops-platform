FROM ubuntu
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=localhost
ENV DEBIAN_FRONTEND=noninteractive

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y lsb-release gnupg2 curl software-properties-common build-essential apt-transport-https git python3-pip && apt-get clean all
RUN add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main"
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add -
RUN apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" -y
RUN apt-get update
RUN apt-get -y install kubectl terraform
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run"]