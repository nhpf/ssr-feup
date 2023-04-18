FROM handsonsecurity/seed-ubuntu:large
ARG DEBIAN_FRONTEND=noninteractive
  
RUN apt-get update \
    && apt-get install -y openvpn openssh-server \
    && apt-get clean

COPY ./ca.crt ./dh.pem ./server.conf ./server.crt ./server.key /vpnfiles/
RUN chmod 400 /vpnfiles/server.key
