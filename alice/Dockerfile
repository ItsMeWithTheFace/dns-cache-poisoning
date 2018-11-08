FROM ubuntu:latest

RUN apt-get update && apt-get install curl gnupg dnsutils iputils-ping net-tools -y && mkdir /app

ADD . /app

WORKDIR /app

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install nodejs -y && npm install

ENTRYPOINT echo 'nameserver 10.0.0.4' > /etc/resolv.conf && npm start
