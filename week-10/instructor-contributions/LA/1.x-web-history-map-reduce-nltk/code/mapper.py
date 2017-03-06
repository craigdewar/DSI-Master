#!/usr/bin/env python

import sys
import string
import urlparse



# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    urls = line.split()
    # increase counters
    for url in urls:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1

	parsed = urlparse.urlparse(url)
        #word = filter(punct, word[0].lower()) #takes the first entry in the list of urls found
        #word = filter(nonum, word.lower())
        print '%s\t%s' % (parsed[1], 1)
