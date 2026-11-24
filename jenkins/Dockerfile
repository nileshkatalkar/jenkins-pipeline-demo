FROM jenkins/jenkins:lts-jdk17
USER root

# Trust the network firewall's certificate (system store and Java)
COPY corp-root.crt /usr/local/share/ca-certificates/fortinet.crt
RUN update-ca-certificates \
    && keytool -importcert -noprompt -trustcacerts -alias fortinet-ca \
       -file /usr/local/share/ca-certificates/fortinet.crt -cacerts -storepass changeit

RUN apt-get -o Acquire::Retries=5 update \
    && apt-get -o Acquire::Retries=5 install -y --no-install-recommends python3 python3-venv docker-cli \
    && rm -rf /var/lib/apt/lists/*