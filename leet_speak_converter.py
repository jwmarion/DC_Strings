#string4.py
import sys
from sys import argv
script, filename = argv

file = open(filename)
text = file.read()
print text

for x in xrange(0,len(text)):
    z = text[x].capitalize()
    if z == "A":
        sys.stdout.write("4")
    elif z == "E":
        sys.stdout.write("3")
    elif z == "G":
        sys.stdout.write("6")
    elif z == "I":
        sys.stdout.write("1")
    elif z == "O":
        sys.stdout.write("0")
    elif z == "S":
        sys.stdout.write("5")
    elif z == "T":
        sys.stdout.write("7")
    else:
        sys.stdout.write(text[x])
