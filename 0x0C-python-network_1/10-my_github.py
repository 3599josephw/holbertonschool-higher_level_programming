#!/usr/bin/python3
"""Displays GitHub id"""

if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    token = sys.argv[2]
    usr = sys.argv[1]
    url = "https://api.github.com/user"

    r = requests.get(url, auth=HTTPBasicAuth(usr, token)).json()
    print(r.get('id'))
