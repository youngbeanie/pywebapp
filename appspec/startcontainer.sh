#!/bin/bash
#$(aws ecr get-login --region us-west-2 | sed 's,https://,,')
echo "home = $HOME id = $(id)"
$(aws ecr get-login --region us-west-2)
docker run --name pywebapp -p 80:8080 --detach 254682475903.dkr.ecr.us-west-2.amazonaws.com/comp4913/pywebapp
