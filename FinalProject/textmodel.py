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
    """ Read the entire contents of a txt file into a string
    """
    f1 = open(filename, "r")  # Open text file for reading
    text = f1.read()  
    f1.close()
    return text

def makeSentenceLengths(s):
    """ creates a dictionary that tracks the number of sentences with a given sentence length
    """
    sentencelengths1 = defaultdict(int)  # default dictionary for counting
    count = 1
    while len(s) != 0:
        if s[0] != "." and s[0] != "?" and s[0] != "!": # if not the end of the sentence
            if s[0] == " ": # if end of a word
                count += 1
        else: # end of a sentence
            sentencelengths1[count] += 1
            count = 0
        s= s[1:]
    return sentencelengths1

def cleanString(s):
    """ removes upper case letters and punctuation marks
    """
    s = s.lower()
    for p in string.punctuation:
        s = s.replace(p, '')
    return s

def makeWordLengths(s):
    """ creates a dictionary that tracks the number of words with given lengths
    """
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
    """ creates a dictionary that tracks the number of times each word appears in the text
    """
    makewordsdict = defaultdict(int)  # default dictionary for counting
    wordList = wordList.split()
    for x in wordList:
        makewordsdict[x] += 1
    return makewordsdict


def makeStems(wordList):
    """ creates a dictionary that tracks the number of times each word stem shows up in a text
    """
    makestemsdict = defaultdict(int)  # default dictionary for counting
    wordList = wordList.split()
    y = ""
    for x in wordList:
        y = porter2.stem(x)
        makestemsdict[x] += 1
    return makestemsdict

def makePunt(s):
    """ creates a dictionary that tracks the number of times that different punctuation marks are used
    """
    punct1 = defaultdict(int)  # default dictionary for counting
    count = 1
    while len(s) != 0:
        if s[0] == "." or s[0] == "?" or s[0] == "!":
            punct1[s[0]] += 1
        s= s[1:]
    return punct1


def main():
    """ takes in text files and outputs measures of vocabulary, word length, word stems, sentence lengths, and punctuation variety
    """
    count = int(input("How many texts would you like to input for learning"))
    yay = ""
    for x in range(count):
        j = input("Enter text file")
        yay += readTextFromFile(j)
    TM = [makeWords(yay), makeWordLengths(yay), makeStems(yay), makeSentenceLengths(yay), makePunt(yay)]
    return printAllDictionaries(TM)

def normalizeDict(d):
    """ Takes in the text model dictionary and normalizes it for the length of the text 
    """
    total = 0
    for x in d:
        total += d[x]
    newd = defaultdict(float)
    for x in d:
        newd[x] = float(d[x]) / float(total)
    return newd

def smallestValue(nd1, nd2):
    """ returns smallest value for each key in two dictionaries
    """
    min = float("inf")
    for x in nd1:
        if nd1[x] < min:
            min = nd1[x]
    for x in nd2:
        if nd2[x] < min:
            min = nd2[x]
    return min

