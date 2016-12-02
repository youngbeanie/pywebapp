#!/bin/bash
docker run --name pywebapp -p 8080:8080 254682475903.dkr.ecr.us-west-2.amazonaws.com/comp4913/pywebapp >>/tmp/pywebapp.log 2>&1 &
