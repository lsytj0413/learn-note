#!/bin/bash

mongo34_start() {
    echo Docker run mongo34 ...
    docker run -d -p :27017:27017 -v mongo34:/data/db --rm --name mongo34 mongo:3.4

    if [ $? -ne 0 ]; then
        echo "Start mongo34 Failed"
        exit 1
    fi
}

mongo34_stop() {
    echo Docker stop mongo34 ...
    docker stop $(docker ps -aq -f "name=mongo34")
}

redis32_start() {
    echo Docker run redis32 ...
    docker run -d -p :6379:6379 --name redis32 --rm redis:3.2

    if [ $? -ne 0 ]; then
        echo "Start redis32 Failed"
        exit 1
    fi
}

# 此处还需要控制 ps 的结果
redis32_stop() {
    echo Docker stop redis32 ...
    docker stop $(docker ps -aq -f "name=redis32")
}

start() {
    echo Start All Docker ...
    mongo34_start
    redis32_start
}

stop() {
    echo Stop All Docker ...
    mongo34_stop
    redis32_stop
}

usage() {
    echo "use start|stop|restart arguments"
}


case $1 in
    start)    start
              exit
              ;;
    stop)     stop
              exit
              ;;
    restart)  stop
              start
              exit
              ;;
    *)        usage
              exit 1
              ;;
esac
