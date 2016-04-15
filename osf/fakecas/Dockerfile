FROM alpine:3.3

MAINTAINER Elliot Metsger <emetsger@jhu.edu>
LABEL description = "Provides a runnning instance of fakecas on port 8080"

RUN mkdir -p /opt/fakecas

WORKDIR /opt/fakecas

COPY fakecas-linux-386 /opt/fakecas/fakecas

RUN chmod 700 fakecas

ENTRYPOINT [ "./fakecas" ]

CMD [ "-dbaddress", "tokumx:27017", "-host", "0.0.0.0:8080" ]
