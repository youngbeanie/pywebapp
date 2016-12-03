#!/bin/bash
$(aws ecr get-login --region us-west-2 | sed 's,https://,,')
