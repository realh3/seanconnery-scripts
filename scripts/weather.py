#!/usr/bin/env python

import urllib
import json
import sys

location = " ".join(sys.argv[1:])
base = "http://api.openweathermap.org/data/2.5/weather?appid=f6b6efffd50eae3e169a2b1ccea7f8fc&units=imperial"
query = urllib.urlencode({'q' : location})
response = urllib.urlopen(base + "&" + query).read()
data = json.loads(response)
weatherDesc = data['weather'][0]['main']
temp = str(data['main']['temp_max'])
print "current weather for " + location + ": " + weatherDesc + ", " + temp + "F"
