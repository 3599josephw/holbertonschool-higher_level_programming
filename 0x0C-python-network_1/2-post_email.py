#!/usr/bin/python3
"""POST request to an email"""

if __name__ == '__main__':

    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('UTF-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()

    print(the_page.decode('UTF-8'))
