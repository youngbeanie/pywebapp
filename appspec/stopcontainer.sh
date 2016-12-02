#!/bin/bash
docker stop pywebapp
CID=$(docker ps -lq)
[ -n "$CID" ] && docker rm $CID
exit 0
