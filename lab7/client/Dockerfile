FROM handsonsecurity/seed-ubuntu:large
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y openvpn openssh-server  \
    && apt-get clean

COPY ./ca.crt ./client.conf ./client1.crt ./client1.key  /vpnfiles/
RUN chmod 400 /vpnfiles/client1.key
