#!/usr/bin/python3
""" print request id """
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    ri = r.headers.get('X-Request-Id')
    print(ri)
