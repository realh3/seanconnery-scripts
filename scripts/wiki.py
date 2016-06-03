#!/usr/bin/env python

import sys, mwclient, unicodedata

MW_URL = "en.wikipedia.org"

def getLink(title):
        return "Read More >> http://" + MW_URL + "/wiki/" + title.replace(" ", "_")

def getInfo(query):
        site = mwclient.Site("en.wikipedia.org")

        data = site.raw_api("query", prop="extracts", exintro=True, explaintext=True, exsentences=3, titles=query)

        page = data["query"]["pages"]
        for k in page.keys():
                return page[k]

if len(sys.argv) <= 2:
        print "nothing to find"
        sys.exit(0)

words = [i.capitalize() for i in sys.argv[2:]]

query = "_".join(words)

data = getInfo(query)
if "missing" in data:
        print "no pages found"
        sys.exit(0)
try:
        if data["extract"].index("REDIRECT") == 0:
                data = getInfo(data["extract"][9:])
                print data["extract"].encode('ascii', 'ignore')
                print getLink(data["title"])
except ValueError as e:
        print data["extract"].encode('ascii', 'ignore')
        print getLink(data["title"])
except Exception as e:
        print "not sure what happened there:"
        print e
