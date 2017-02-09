#string6.py

import sys

text = "lbh zhfg hayrnea jung lbh unir yrnearq"
myList = []

for x in xrange(0,len(text)):
    myList.append(ord(text[x])+13)
    if myList[len(myList) - 1] > 122:
        myList[len(myList) - 1] = myList[len(myList) -1] - 26
    myList[len(myList) - 1] = chr(myList[len(myList) - 1])

for x in xrange(0,len(myList)):
    sys.stdout.write(myList[x])
print ""
