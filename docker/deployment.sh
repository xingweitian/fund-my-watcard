#!/bin/sh

set -e

VERSION=$1
USERNAME="faushine"

docker build --no-cache -t $USERNAME/fund-my-watcard:$VERSION .

docker push $USERNAME/fund-my-watcard:$VERSION

exit
