
#!/usr/bin/env python
import random
import string
testText = "The woman now gave Dorothy a bed to sleep in, and Toto lay down beside her, while the Lion guarded the door of her room so she might not be disturbed. The Scarecrow and the Tin Woodman stood up in a corner and kept quiet all night, although of course they could not sleep."

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
    print newText

cutUp(testText)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
