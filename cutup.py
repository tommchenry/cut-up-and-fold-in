#!/usr/bin/env python
import random
import string
from sys import argv

#Takes import and export filename as an argument.
script, infilename, outfilename = argv 
inFile = open(infilename, 'r', 0)
outFile = open(outfilename, 'w')
cutText = inFile.read()

print "Cutting up %r." % infilename
print "Exporting to %r." % outfilename

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
    outFile.write(' '.join(newText))
    inFile.close()
    outFile.close()
cutUp(cutText)
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
