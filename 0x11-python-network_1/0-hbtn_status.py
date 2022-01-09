#!/usr/bin/python3
""" what's my status """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        bc = response.read()
        bt = type(response.read())
        bu = bc.decode(encoding='UTF-8')
        print('Body response:')
        print('\t- type: {}'.format(bt))
        print('\t- content: {}'.format(bc))
        print('\t- utf8 content: {}'.format(bu))
