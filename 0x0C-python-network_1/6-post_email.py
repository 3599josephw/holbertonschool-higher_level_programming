#!/usr/bin/python3
"""POST request to an email"""

if __name__ == '__main__':

    import requests
    import sys

    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    r = requests.post(url, data=payload)

    print(r.text)
