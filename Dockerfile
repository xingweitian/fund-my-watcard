# Base image to use, this must be set as the first line
FROM ubuntu

LABEL maintainer="fyuxin@uwaterloo.ca"

# Commands to update the image
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libfontconfig \
    libgconf2-4 \
    libglib2.0-0 \
    libnss3 \
    libx11-6 \
    build-essential \
    python-dev \
    python-setuptools \
    python-pip \
    python-smbus \
    libncursesw5-dev \
    libgdbm-dev \
    libc6-dev \
    zlib1g-dev \
    libsqlite3-dev \
    libssl-dev \
    openssl \
    libffi-dev

WORKDIR /usr/local/share/
RUN wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && chmod +x chromedriver \
    && ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver \
    && ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

WORKDIR /tmp/
RUN wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0b3.tar.xz \
    && tar xpvf Python-3.7.0b3.tar.xz \
    && cd Python-3.7.0b3/ \
    && ./configure --prefix /usr/local/ \
    && make \
    && make altinstall \
    && ln -s /usr/local/bin/python3.7 /usr/bin/python37 \
    && ln -s /usr/local/bin/pip3.7 /usr/bin/pip37 \
    && pip3.7 install fund-my-watcard 
