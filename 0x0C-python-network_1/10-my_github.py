#!/usr/bin/python3
"""Displays GitHub id"""

if __name__ == '__main__':
    import requests
    import sys

    token = sys.argv[2]
    user = sys.argv[1]
    url = "https://api.github.com/users/{}".format(user)

    headers = {'Authorization': f'token {token}'}

    r = requests.get(url, headers=headers).json()
    print(r.get('id'))
