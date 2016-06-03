#!/usr/bin/env python
#Check Dr. Tyson's twitter status
import twitter, random, time

a = twitter.Api(
    consumer_key=##
    consumer_secret=##
    access_token_key=##
    access_token_secret=##
)

t = a.GetUserTimeline(screen_name='neiltyson', count=30)

r = random.Random()
r.seed(time.time())
print 'Badass Dr. T: ' + r.choice(t).text.encode('utf8').strip()

