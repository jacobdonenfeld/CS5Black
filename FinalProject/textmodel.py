#TextModel project!
#
# name(s): Jacob Donenfeld, Athena Li
#

from collections import defaultdict
import string
from stemming import porter2


def printAllDictionaries( TM ):
    """ a function to print all of the dictionaries in TM
        input: TM, a text model (a list of 5 or more dictionaries)
    """
    words = TM[0]
    wordlengths = TM[1]
    stems = TM[2]
    sentencelengths = TM[3]
    punct = TM[4]

    print("\nWords:\n", words)
    print("\nWord lengths:\n", wordlengths)
    print("\nStems:\n", stems)
    print("\nSentence lengths:\n", sentencelengths)
    print("\nEndings\n", punct)

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


def makeStems(wordList):
    makestemsdict = defaultdict(int)  # default dictionary for counting
    wordList = wordList.split()
    y = ""
    for x in wordList:
        y = porter2.stem(x)
        makestemsdict[x] += 1
    return makestemsdict

def makePunt(s):
    punct1 = defaultdict(int)  # default dictionary for counting
    count = 1
    while len(s) != 0:
        if s[0] == "." or s[0] == "?" or s[0] == "!":
            punct1[s[0]] += 1
        s= s[1:]
    return punct1


def main():
    count = int(input("How many texts would you like to input for learning"))
    yay = ""
    for x in range(count):
        j = input("Enter text file")
        yay += readTextFromFile(j)
    TM = [makeWords(yay), makeWordLengths(yay), makeStems(yay), makeSentenceLengths(yay), makePunt(yay)]
    return printAllDictionaries(TM)

def normalizeDict(d):
    total = 0
    for x in d:
        total += d[x]
    newd = defaultdict(float)
    for x in d:
        newd[x] = float(d[x]) / float(total)
    return newd

def smallestValue(nd1, nd2):
    min = float("inf")
    for x in nd1:
        if nd1[x] < min:
            min = nd1[x]
    for x in nd2:
        if nd2[x] < min:
            min = nd2[x]
    return min



d1 = {'a': 5, 'b':1, 'c':2}
nd1 = normalizeDict( d1 )
d2 = {'a': 15, 'd':1}
nd2 = normalizeDict( d2 )
print("The normalized dictionaries are")
print(nd1)
print(nd2)
sm_va = smallestValue( nd1, nd2 )
print("and the smallest value between them is", sm_va)




# and, test things out here...
#print("TextModel1:")
#printAllDictionaries( TextModel1 )