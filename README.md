# DNS Cache Poisoning Attack Demo
## Introduction
The purpose of this repository is to showcase the famous [Kaminsky Attack](http://unixwiz.net/techtips/iguide-kaminsky-dns-vuln.html) which enables a remote hacker to poison the cache of a vulnerable DNS server remotely to redirect users to malicious IP addresses.

## Setup
We have 3 entities participating in the attack:\
`Alice` (`10.0.0.2`): The unsuspecting user who will query the poisoned DNS server\
`Mallory` (`10.0.0.3`): The remote hacker who poisons the DNS server\
`Server` (`10.0.0.4`): The vulnerable DNS server

In order to build the project, run the following commands:
1. Build the images
   ```bash
   docker-compose build
   ```
2. Create the containers
   ```bash
   docker-compose up
   ```
3. Go into Mallory
   ```bash
   docker exec -it mallory bash
   ```
4. Run the following command
   ```bash
   python3 /shared/mallory/attack.py
   ```
5. Let the attack run and restart Mallory after some time
6. If Alice tries to query `sec-commerce.seclab.space` she'll get Mallory's IP

## Explanation
Essentially what `attack.py` does is create 10 processes, each of which queries the DNS server to trigger the recursive resolution of the fake hostname and sends 50 fake response packets every few milliseconds. The intention is that the DNS server accepts one of these fake response packets and caches the result so that when Alice tries to query the same hostname, she'll get redirected to the spoofed address.
