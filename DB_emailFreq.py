#!/usr/bin/python

"""
Title: Database - Email-Domain Frequency Counter
Author: Insider
Made with stackoverflow copypasta.
Engine: Python 3.x
"""

# Libraries
import re
import string
from collections import Counter
import json

# Input Database File
dataFile = input("File: ")

# Variable declaritions, Regex Definitions & parsing
frequency = {}
document_text = open(dataFile, 'r')
text_string = document_text.read().lower()
text_string_raw = document_text.read()
match_pattern = re.findall(r'@[\w.]+', text_string)

# Pattern regex 
lst = match_pattern

# Parsing
s = []
s += ([s.replace('@', '') for s in lst])

# Frequency Counting
counts = Counter(s)

# Dictionary Storage
o = dict(counts)

# Json Datastructure
dataFile = "src = " + dataFile
a = ({"domain":"frequency",dataFile:[{'domain':key,"frequency":value} for key,value in o.items()]})

# Write and parse to json
d = {"domain":"frequency","":[{'domain':key,"frequency":value} for key,value in o.items()]}
with open('emailFreq.json', 'w') as fn:
	json.dump(d, fn)