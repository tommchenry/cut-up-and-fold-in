#!/usr/bin/env python
import random
import string
from sys import argv

#Takes import and export filename as an argument.
script, infilename, outfilename = argv 
inFile = open(infilename, 'r', 0)
outFile = open(outfilename, 'w')
cutText = inFile.read()

def cutUp(text, breakFreq = 20, phraseMax = 3):
    """
    Takes a text string and returns a text string with words scrambled into 
    random order, approximating a basic cut-up.
    """
    newText=[]
    textCopy=list(text)
    for i in range(len(text)):
        selectedWord=random.randrange(0, len(textCopy))
        phraseSave = random.randrange(0, phraseMax)
        if selectedWord + phraseSave < len(textCopy):    
            for i in range (0,phraseSave):
                newText.append(textCopy[selectedWord + i])
                textCopy.remove(textCopy[selectedWord + i])
        if random.randrange(0, breakFreq) == breakFreq - 1: 
                newText.append('\n')
    return ' '.join(newText)

def startProg(text):
    '''
    The core display function. This takes user input to regulate the mangling of
    text.
    '''
    runProg = True
    print 'Text Mangler 0.7'
    while runProg == True: 
        text = text.split()
        previewText = ""
        print 'Current Text: %r' % infilename
        print '------------'
        for i in range (0,30):
            previewText+=text[i] + " "
            if i > 1 and i % 10 == 0:
                previewText+='\n'
        previewText+= "[MORE]"
    #print ' '.join(previewText) 
        print previewText
        command = raw_input('(C to perform cut-up, X to exit):>')
        if command == 'X' or command == 'x':
            print 'Exiting.'
            runProg = False
        if command == 'C' or command == 'c':
            print 'Cutting Up.'
            breakFreq = raw_input('Line break frequency:>')
            try: 
                breakFreq = int(breakFreq)
            except ValueError:
                print '%r is not a valid integer, substituting 20' % breakFreq
                breakFreq = 20
            phraseMax = raw_input('Maximum original phrase length:>')
            try: 
                phraseMax = int(phraseMax)
            except ValueError:
                print '%r is not a valid integer, substituting 4' % phraseMax
                phraseMax = 4
            text = cutUp(text, breakFreq, phraseMax)
            outFile.write(text)
    inFile.close()
    outFile.close()

startProg(cutText)
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
