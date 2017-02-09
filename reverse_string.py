#string3.py

import sys

mess = raw_input("Enter a string: ")

for x in xrange(len(mess)-1, -1, -1):
    sys.stdout.write(mess[x])
print("")
