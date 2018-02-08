# node enviroment
FROM ubuntu:16.04

MAINTAINER yangsl2

# change default shell
# SHELL ["/bin/bash", "-c"]

COPY ./sources.list /etc/apt/sources.list

ENV NVM_DIR /root/.nvm
# fix nvm ls-remote only list iojs version
ENV NVM_NODEJS_ORG_MIRROR http://npm.taobao.org/mirrors/node

WORKDIR /root

RUN apt-get update \
    && apt-get install -y curl \
    && curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install 9.3.0 \
    && nvm use 9.3.0 \
    && npm config set registry https://registry.npm.taobao.org \
    && npm install -g pm2 yarn \
    && yarn config set registry https://registry.npm.taobao.org \
    && apt-get remove -y curl \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# use pm2-docker command to start node app
CMD ["/bin/bash"]
