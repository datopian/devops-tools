FROM datopian/ckan:ckan-2.8.9

USER root

RUN echo http://dl-cdn.alpinelinux.org/alpine/v3.10/main >> /etc/apk/repositories
RUN apk add --no-cache postgresql-client=11.12-r0

RUN wget https://dl.min.io/client/mc/release/linux-amd64/mc -O /usr/local/bin/mc || curl https://dl.min.io/client/mc/release/linux-amd64/mc --output /usr/local/bin/mc
RUN chmod +x  /usr/local/bin/mc


