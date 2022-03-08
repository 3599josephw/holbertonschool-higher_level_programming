#!/usr/bin/python3
"""Catches HTTP errors"""

if __name__ == '__main__':
    from urllib import request
    from urllib.error import HTTPError
    import sys

    try:
        with request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('UTF-8'))
    except HTTPError as e:
        print('Error code: ', e.code)
