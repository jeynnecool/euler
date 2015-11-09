import os
import re

indir = 'C:\Dropbox\euler'

for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        if re.match('^[0-9][0-9][0-9]\.py', f):
        	os.rename(f, 'problem'+f)
        	