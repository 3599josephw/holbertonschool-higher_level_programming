#!/usr/bin/python3
"""Catches HTTP errors"""

if __name__ == '__main__':
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
