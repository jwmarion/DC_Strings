#string5.py

import sys

mess = raw_input("Enter a word: ")

for x in xrange(0, len(mess)):
    a = mess[x].capitalize()
    if a == 'A' or a =='E' or a == 'I' or a == 'O' or a == 'U':
        for y in xrange(0,5):
            sys.stdout.write(mess[x])
    else:
        sys.stdout.write(mess[x])
