#!/usr/bin/python3
""" send POST request to github """
import requests
import sys


if __name__ == "__main__":
    response = requests.get("https://api.github.com/user", auth=(
        sys.argv[1], sys.argv[2]))
    result = response.json()
    print(result.get("id"))
