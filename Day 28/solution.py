#!/bin/python

import sys
import re

N = int(raw_input().strip())
names = []
for a0 in xrange(N):
    firstName,emailID = raw_input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    
    if re.search(r"@gmail\.com$", emailID):
        names.append(firstName)

names.sort()
for name in names:
    print(name)