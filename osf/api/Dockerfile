FROM python:2.7

RUN usermod -d /home www-data && chown www-data:www-data /home

# Install dependancies
RUN apt-get update \
    && apt-get install -y \
        git \
        libev4 \
        libev-dev \
        libevent-dev \
        libxml2-dev \
        libxslt1-dev \
        zlib1g-dev \
        # cryptography
        build-essential \
        libssl-dev \
        libffi-dev \
        python-dev \
        # for debugging and sanity
        strace \
        lsof \
        net-tools \
        tcpdump \
        curl \
        vim \
        less \
        iptables \
        telnet \
    && apt-get clean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# grab gosu for easy step-down from root
ENV GOSU_VERSION 1.4
RUN apt-get update \
    && gpg --keyserver pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
  	&& curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
  	&& gpg --verify /usr/local/bin/gosu.asc \
  	&& rm /usr/local/bin/gosu.asc \
  	&& chmod +x /usr/local/bin/gosu \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Node : https://registry.hub.docker.com/u/library/node/
ENV NODE_VERSION 0.12.4
ENV NPM_VERSION 2.10.1
RUN apt-get update \
    && gpg --keyserver pool.sks-keyservers.net --recv-keys 7937DFD2AB06298B2293C3187D33FF9D0246406D 114F43EE0176B71C7BC219DD50A3051F888C628D \
    && curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
  	&& curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  	&& gpg --verify SHASUMS256.txt.asc \
  	&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc | sha256sum -c - \
  	&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
  	&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \
  	&& npm install -g npm@"$NPM_VERSION" \
  	&& npm cache clear \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV SOURCE_BRANCH develop
# ENV SOURCE_BRANCH master
ENV SOURCE_REPO https://github.com/emetsger/osf.io.git
ENV WHEELHOUSE /home/.cache/wheelhouse
ENV DJANGO_SETTINGS_MODULE api.base.settings
ENV UPDATE_CMD 'invoke clean && invoke wheelhouse --release && invoke requirements --release && gosu www-data invoke assets && gosu www-data python manage.py collectstatic --noinput'

RUN pip install -U pip

RUN pip install \
      invoke==0.11.0 \
      uwsgi==2.0.10

WORKDIR /code

RUN chmod g+rwx /code && chgrp www-data /code

# perform an initial build to cache long running compilations
RUN gosu www-data git clone -b $SOURCE_BRANCH $SOURCE_REPO . \
    && gosu www-data git config user.email emetsger@jhu.edu \
    && gosu www-data git config user.name "Elliot Metsger <OSF API Docker Container>" \
    && cp website/settings/local-dist.py website/settings/local.py \
    && chown -R www-data:www-data /code

RUN invoke wheelhouse --release
RUN invoke requirements --release

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8000
VOLUME /code

RUN chown -R www-data:www-data /home || true
RUN chown -R www-data:www-data /code || true

CMD ["invoke", "apiserver", "--host", "0.0.0.0"]
