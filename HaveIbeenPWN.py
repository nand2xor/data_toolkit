#!/usr/bin/python

"""
Title: HaveIBeenPWN API-Wrapper (to fetch DB-list)
Author: Insider
Made with stackoverflow copypasta.
Engine: Python 3.x
"""

# Libraries
from collections import Counter
import json
import urllib.request

# Request
url = "https://haveibeenpwned.com/api/v2/breaches"
req = urllib.request.Request(url,data=None,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

# Decode & Parse
r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
counter = 0

# Writing to outfile
with open('haveIbeenPWN.json', 'w', encoding='utf8') as ou:
	json.dump(cont, ou, indent=4)
		