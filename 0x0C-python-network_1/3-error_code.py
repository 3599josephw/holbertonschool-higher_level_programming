#!/usr/bin/python3
"""Catches HTTP errors"""

if __name__ == '__main__':
    from urllib import request, error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
