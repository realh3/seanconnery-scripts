#!/usr/bin/env python

# use it to create tables for use with other scripts (see sean.sh)

import MySQLdb as mdb
import sys

con = None

tables = ['mfw-phrases', 'phrases', 'status']

if len(sys.argv) < 3:
        print "need table and item to add"
        sys.exit(0)

if sys.argv[1] not in tables:
        print sys.argv[1], "table not found?"
        sys.exit(0)

table = sys.argv[1]
item = ' ' .join(sys.argv[2:])

try:
        con = mdb.connect('localhost', 'seanconnery', '', 'eggdrop')

        cur = con.cursor()
        cur.execute("INSERT INTO " + table + " (phrase) VALUES (%s)", (item))
        print "done"
except mdb.Error, e:
        print "error %d: %s " % (e.args[0], e.args[1])

finally:
        if con:
                con.close()
