#!/usr/bin/env python

import sys
import string

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        punct = lambda x:x not in string.punctuation
        nonum = lambda x:x not in string.digits

        word = filter(punct, word.lower())
        word = filter(nonum, word.lower())
        print '%s\t%s' % (filter(punct, word.lower()), 1)
