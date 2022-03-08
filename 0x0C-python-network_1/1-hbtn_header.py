#!/usr/bin/python3
"""takes a URl, sends request, displays the value of X-Request-Id"""

if __name__ == '__main__':

    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()

    print(html.get('X-Request-Id'))
