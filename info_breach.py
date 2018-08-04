#!/usr/bin/python

"""
Title: Information-Is-Beautiful GoogleDrive DB-List Fetcher
Author: Insider
Made with stackoverflow copypasta.
Engine: Python 3.x
"""

# Libraries
import urllib.request
import http.cookiejar
from urllib.request import build_opener, HTTPCookieProcessor

# Prepare cookie & request
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(HTTPCookieProcessor(cj))
resp = opener.open('https://docs.google.com/spreadsheet/ccc?key=1Je-YUdnhjQJO_13r8iTeRxpU2pBKuV6RVRHoYCgiMfg&output=csv')

# Write data in chunks to outfile
CHUNK = 16 * 1024
with open('info_breaches.csv', 'wb') as f:
    while True:
        chunk = resp.read(CHUNK)
        if not chunk:
            break
        f.write(chunk)

