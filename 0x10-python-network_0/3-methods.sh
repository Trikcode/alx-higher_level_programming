#!/bin/bash
# display methods
curl -si -X "OPTIONS" $1 | grep "Allow" | cut -d " " -f 2-
