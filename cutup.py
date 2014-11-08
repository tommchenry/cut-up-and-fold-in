#!/usr/bin/env python
import random
import string
from sys import argv

script, filename = argv 
inFile = open(filename, 'r', 0)
cutText = inFile.read()

print "Cutting up %r." % filename

def cutUp(text):
    """
    Takes a text string and returns a text string with words scrambled into 
    random order, approximating a basic cut-up.
    """
    text = text.split()
    newText=[]
    textCopy=list(text)
    for i in range(len(text)):
        selectedWord=random.randrange(0, len(textCopy))
        newText.append(textCopy[selectedWord])
        textCopy.remove(textCopy[selectedWord])
    print ' '.join(newText) 
    inFile.close()
cutUp(cutText)
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
