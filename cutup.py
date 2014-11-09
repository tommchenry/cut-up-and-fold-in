#!/usr/bin/env python
import random
import string
from sys import argv

#Takes import and export filename as an argument.
script, infilename, outfilename = argv 
inFile = open(infilename, 'r', 0)
cutText = inFile.read()

def cutUp(text, breakFreq = 20, phraseMax = 3):
    """
    Takes a text string and returns a text string with words scrambled into 
    random order, approximating a basic cut-up.
    """
    newText=[]
    textCopy=list(text)
    lastWord = ''
    chapterCount = 1 

    try:
        for i in range(len(text)):
            selectedWord = pickWord(lastWord, textCopy)
            if textCopy[selectedWord] != 'Chapter':    
                phraseSave = random.randrange(0, phraseMax)
                newGraph = False
                nextWord = textCopy[selectedWord]
                #Checks to see if a line ends in a period, chance to start new graf
                for letter in nextWord:
                    if letter == '.' and nextWord != 'Mr.' and nextWord != 'Mrs.':
                        if random.randrange(0, breakFreq) == breakFreq - 1: 
                            newGraph = True
                #If a new graph is created, appends word and a double linebreak
                if newGraph == True:
                    newText.append(textCopy[selectedWord])
                    newText.append('\n\n')
                    textCopy.remove(textCopy[selectedWord])
                    lastWord = ''
                    newGraph = False
                #Otherwise, if the phrase can fit in the remaining file, it appends
                elif selectedWord + phraseSave < len(textCopy) - 1 and phraseSave > 1:    
                    lastWord = textCopy[selectedWord + phraseSave]
                    for i in range (0,phraseSave):
                        newText.append(textCopy[selectedWord + i])
                    for i in range (0, phraseSave):
                        textCopy.remove(textCopy[selectedWord])
                else: 
                    newText.append(textCopy[selectedWord])
                    lastWord = textCopy[selectedWord]
                    textCopy.remove(textCopy[selectedWord])
            else:

                newText.append('\n\n')
                newText.append('Chapter')
                newText.append(str(chapterCount))
                newText.append('\n\n')
                chapterCount += 1
                print 'remove:', textCopy[selectedWord]
                textCopy.remove(textCopy[selectedWord])
                print 'remove:', textCopy[selectedWord]
                textCopy.remove(textCopy[selectedWord])
            if len(textCopy) == 0:
                    break


    except IndexError:
        print 'Borked!:'
        print 'i =', i, 'selectedWord =', selectedWord 
        print 'The word is', textCopy[selectedWord]
        print 'phraseSave =', phraseSave, 'Remain =', len(textCopy)
        
    return ' '.join(newText)

def pickWord (lastWord,text):
    '''
    Picks a random word from a list text that is not the string lastWord
    '''
    selectedWord = random.randrange(0, len(text))
    nextWord = text[selectedWord]
    if nextWord == lastWord: 
        return pickWord (lastWord, text)
    else:
        return selectedWord
    
def startProg(text):
    '''
    The core display function. This takes user input to regulate the mangling of
    text.
    '''
    runProg = True
    print 'Text Mangler 0.7'
    text = text.split()
    while runProg == True: 
        if isinstance(text, basestring):
           text = text.split() 
        previewText = ""
        print 'Current Text: %r' % infilename
        print '------------'
        if len(text) > 50:
            for i in range (0,50):
                previewText+=text[i] + " "
                if i > 1 and i % 10 == 0:
                    previewText+='\n'
            previewText+= "[MORE]"
        else:
            for i in range (0,len(text)):
                 previewText+=text[i] + " "
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
                print '%r is not a valid integer, substituting 5' % breakFreq
                breakFreq = 5
            phraseMax = raw_input('Maximum original phrase length:>')
            try: 
                phraseMax = int(phraseMax)
            except ValueError:
                print '%r is not a valid integer, substituting 1' % phraseMax
                phraseMax = 1
            text = cutUp(text, breakFreq, phraseMax)
            outFile = open(outfilename, 'w')
            outFile.write(text)
            outFile.close()
    inFile.close()


startProg(cutText)
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
