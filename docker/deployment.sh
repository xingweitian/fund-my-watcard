#!/bin/sh
# fill in this configuration before run.
VERSION=""
USERNAME=""

# build from docker file
cd docker

docker build --no-cache -t $USERNAME/fund-my-watcard:$VERSION .

docker push $USERNAME/fund-my-watcard:$VERSION

exit
