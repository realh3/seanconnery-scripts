#!/usr/bin/python

import random
import sys

el1, el2 = "", ""
thing = " ".join(sys.argv[1:])

if thing[0:len("level")] == "level":
    thing = thing[len("level"):]

if "/" in thing:
    el1, el2 = thing.split("/")
else:
    el1 = thing

def genLines():
    total_length = 15
    idx = random.randint(0, total_length)
    lines = ""
    for i in range(0, total_length + 1):
        if idx == i:
            lines += "[X]"
        else:
            lines += "-"
    return lines

print "{0} |{1}| {2}".format(el1, genLines(), el2)
