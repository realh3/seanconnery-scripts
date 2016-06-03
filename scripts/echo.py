#!/usr/bin/env python

import sys, re

who = ''
if len(sys.argv) > 2:
	who = sys.argv[1]
	sys.argv.remove(who)

input = sys.argv[1:][0]

if input.find('echo') == 0:
	if len(who):
		print who + " wants me to say: " + input[len('echo'):].strip()
	else:
		print input[len('echo'):].strip()
	sys.exit(0)

if len(who):
	print who + " wants me to say: " + input.strip()
else:
	print input.strip()
