#!/usr/bin/env python

import urllib
import json as m_json
import re
import sys
from time import sleep

response = urllib.urlopen ( 'https://opentdb.com/api.php?amount=1&difficulty=medium&type=multiple' ).read()
json = m_json.loads ( response )
if json == None or json['results'] == None:
    print "Why was there an API error?"
    sys.exit(0)

results = json [ 'results' ]

if len(results) == 0:
    print "Why was there an API error?"
    sys.exit(0)

result = results[0]
question = result['question']
answer = result['correct_answer']
try:
    print question
    sleep(2)
    print "[Answer revealed in fifteen seconds]"
    sleep(14)
    print ( "Answer: " + answer )

except:
    print "Why does Ian suck at programming?"
