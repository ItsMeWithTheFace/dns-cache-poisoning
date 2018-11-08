FROM ubuntu:latest

RUN apt-get update && apt-get install dnsutils dsniff iptables net-tools python python3 wget iputils-ping nmap libdnet python3-pip git tcpdump -y

RUN pip3 install scapy-python3
RUN pip3 install scapy-http

ENTRYPOINT echo 'nameserver 10.0.0.4' > /etc/resolv.conf && /bin/bash
