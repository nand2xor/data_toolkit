#!/usr/bin/python

"""
Title: vigilante.pw Database list Fetcher (API_Wrapper)
Author: Insider
Made with stackoverflow copypasta.
Engine: Python 3.x
"""

# Libraries
import re
import string
import urllib.request, urllib.error, urllib.parse,http.cookiejar
# from html.parser import HTMLParser
# from xml.etree.ElementTree import fromstring

# Request Data
site= "https://vigilante.pw/"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

# Request
req = urllib.request.Request(site, headers=hdr)

# Fetch Data
try:
    page = urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.fp.read())

# Read and decode data to utf
content = page.read().decode('utf-8')
with open('output.html', 'w') as f:
    f.write(content)

# Creating empty block to write parsed data into
data_file = open("output.html")
block = ""
found = False

# Parse HTML for only table
for line in data_file:
    if found:
        block += line
        if line.strip() == "</tbody>": break
    else:
        if line.strip() == "<tbody>":
            found = True
            block = "</tbody>"

# Close file
data_file.close()

# Hacky fix, add missing tags and correct the html
a_str = block.replace("<tbody>", "\n</tbody>\n</table>", 1)
with open('parsed.html', 'w') as f:
    f.write(a_str)
	
# Add missing tags and correct the html. And also adding the thead data.
b_str = block.replace("</tbody>", '<table>\n<thead>\n<tr role="row"><th data-field="entries" class="sorting" tabindex="0" aria-controls="breaches-table" rowspan="1" colspan="1" style="width: 148px;" aria-label="Entries: activate to sort column descending">Entries</th><th data-field="name" class="sorting" tabindex="0" aria-controls="breaches-table" rowspan="1" colspan="1" style="width: 249px;" aria-label="Database: activate to sort column ascending">Database</th><th data-field="encryption" class="sorting" tabindex="0" aria-controls="breaches-table" rowspan="1" colspan="1" style="width: 249px;" aria-label="Hashing Algorithm: activate to sort column ascending">Hashing Algorithm</th><th data-field="category" class="sorting" tabindex="0" aria-controls="breaches-table" rowspan="1" colspan="1" style="width: 249px;" aria-label="Category: activate to sort column ascending">Category</th><th data-field="date" class="sorting_desc" tabindex="0" aria-controls="breaches-table" rowspan="1" colspan="1" style="width: 135px;" aria-sort="descending" aria-label="Dump Date: activate to sort column ascending">Dump Date</th><th data-field="date" class="sorting" tabindex="0" aria-controls="breaches-table" rowspan="1" colspan="1" style="width: 189px;" aria-label="Acknowledged?: activate to sort column ascending">Acknowledged?</th></tr>\n</thead>\n<tbody>', 1)
with open('parsed.html', 'w') as f:
    f.write(b_str)
	
# Fix incorrect tags	
with open("parsed.html", "a") as myfile:
    myfile.write("</table>")

