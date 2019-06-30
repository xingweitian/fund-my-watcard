# Base image to use, this must be set as the first line
FROM ubuntu

# Maintainer: docker_user <docker_user at email.com> (@docker_user)
MAINTAINER faushine fyuxin@uwaterloo.ca

# Commands to install python
RUN apt-get update \
    && apt-get install -y python3-pip python3-dev vim curl apt-utils \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip \
    && pip install fund-my-watcard

# Commands to install Chrome and chromedriver
RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb \
    && dpkg -i /chrome.deb || apt-get install -yf \
    && rm /chrome.deb \
    && curl https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip -o /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver

# Commands to add source code to container for test
# ADD ./ /usr/local/share/fund_my_watcard

# Commands to add config file to container for test
# ADD .watcard_config /root/.watcard_config

# Commands to add config file to container
ADD .watcard_config ~/.watcard_config