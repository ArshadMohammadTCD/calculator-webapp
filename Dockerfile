FROM ubuntu:latest
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y python3
