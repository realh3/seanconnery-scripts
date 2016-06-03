#!/usr/bin/env python

import urllib
import json as m_json
import re
import sys

if sys.argv[1] == ".google" or sys.argv[1] == ".bing":
    query = ' '.join(sys.argv[2:])
else:
    query = ' '.join(sys.argv[1:])

query = urllib.urlencode ( { 'q' : query } )
response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
json = m_json.loads ( response )
if json == None or json['responseData'] == None:
        print "nothing found"
        sys.exit(0)

results = json [ 'responseData' ] [ 'results' ]

if len(results) == 0:
        print "nothing found"
        sys.exit(0)

result = results[0]
title = re.sub('<[^<]+?>', '', result['title'])
url = result['url']   # was URL in the original and that threw a name error exception
try:
        print ( title + ': ' + url )
except:
        print url
