#!/usr/bin/python3
""" post email """
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        ce = response.read().decode(encoding='UTF-8')
        print(ce)
