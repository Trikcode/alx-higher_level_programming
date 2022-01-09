#!/usr/bin/python3
""" print error code """
import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        urllib.request.urlopen(req)
        with urllib.request.urlopen(req) as response:
            bc = response.read().decode('utf-8')
            print(bc)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
