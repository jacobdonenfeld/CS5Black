#TextModel project!
#
# name(s): Jacob Donenfeld, Athena Li
#

from collections import defaultdict
import string
from stemming.porter2 import stem

# TextModel1 = [ ]  # start with the empty list
#
# words1 = defaultdict( int )  # default dictionary for counting
# TextModel1 = TextModel1 + [ words1 ]  # add that dictionary in...
#
# wordlengths1 = defaultdict( int )  # default dictionary for counting
# TextModel1 = TextModel1 + [ wordlengths1 ]  # add that dictionary in...
#
# stems1 = defaultdict( int )  # default dictionary for counting
# TextModel1 = TextModel1 + [ stems1 ]  # add that dictionary in...
#
# sentencelengths1 = defaultdict( int )  # default dictionary for counting
# TextModel1 = TextModel1 + [ sentencelengths1 ]  # add that dictionary in...

# create one of your own...
# words1 = defaultdict( int )  # default dictionary for counting
# TextModel1 = TextModel1 + [ words1 ]  # add that dictionary in...

# a function to print all of the dictionaries in a TextModel1

def printAllDictionaries( TM ):
    """ a function to print all of the dictionaries in TM
        input: TM, a text model (a list of 5 or more dictionaries)
    """
    words = TM[0]
    wordlengths = TM[1]
    stems = TM[2]
    sentencelengths = TM[3]

    print("\nWords:\n", words)
    print("\nWord lengths:\n", wordlengths)
    print("\nStems:\n", stems)
    print("\nSentence lengths:\n", sentencelengths)
    print("\n\n")

def readTextFromFile(filename):
    f1 = open(filename, "r")  # Open text file for reading
    text = f1.read()  # Read the entire contents of the file into a string
    f1.close()
    return text

def makeSentenceLengths(s):
    sentencelengths1 = defaultdict(int)  # default dictionary for counting
    count = 1
    while len(s) != 0:
        if s[0] != "." and s[0] != "?" and s[0] != "!":
            if s[0] == " ":
                count += 1
        else:
            sentencelengths1[count] += 1
            count = 0
            print("ding")
        s= s[1:]
    return sentencelengths1

def cleanString(s):
    s = s.lower()
    for p in string.punctuation:
        s = s.replace(p, '')
    return s

def makeWordLengths(s):
    wordlengths1 = defaultdict(int)  # default dictionary for counting
    count = 1
    while len(s) != 0:
        if s[0] != " ":
            count += 1
        else:
            wordlengths1[count] += 1
            count = 0
        s = s[1:]
    return wordlengths1

def makeWords(wordList):
    makewordsdict = defaultdict(int)  # default dictionary for counting
    wordList = wordList.split()
    for x in wordList:
        makewordsdict[x] += 1
    return makewordsdict

# include other functions here...


# and, test things out here...
#print("TextModel1:")
#printAllDictionaries( TextModel1 )

