#!/bin/bash
# display methods
curl -s -o /dev/null -w "%{http_code}" $1
