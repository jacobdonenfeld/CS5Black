#TextModel project!
#
# name(s): Jacob Donenfeld, Athena Li
#

from collections import defaultdict
import string
from stemming import porter2
import math


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

def makePunct(s):
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
    TM = [makeWords(yay), makeWordLengths(yay), makeStems(yay), makeSentenceLengths(yay), makePunct(yay)]
    return printAllDictionaries(TM)

def normalizeDictionary(d):
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

def compareDictionaries(d, nd1, nd2):
    """ computes log-probability that dictionary d came from nd1 or nd2, two normalized dictionaries
    """
    totalnd1 = 0.0
    totalnd2 = 0.0
    epsilon = smallestValue(nd1, nd2) /2.0
    for x in d:
        if x in nd2:
            if x in nd1:
                val = 2 * math.log(min(nd1[x], nd2[x]))
                totalnd1 += d[x] * math.log(nd1[x])
                totalnd2 += d[x] * math.log(nd2[x])
            else:
                totalnd2 += d[x] * math.log(nd2[x])
                totalnd1 += d[x] * math.log(epsilon)
        elif x in nd1:
            totalnd1 += d[x] * math.log(nd1[x])
            totalnd2 += d[x] * math.log(epsilon)
        else:
            totalnd1 += d[x] * math.log(epsilon)
            totalnd2 += d[x] * math.log(epsilon)
    return [totalnd1, totalnd2]

def createAllDictionaries(s): 
        """ should create out all five of a string's 
            dictionaries in full - for testing and 
            checking how they are working...
        """
        sentencelengths = makeSentenceLengths(s)
        new_s = cleanString(s)
        words = makeWords(new_s)
        stems = makeStems(new_s)
        punct = makePunct(s)
        wordlengths = makeWordLengths(new_s)
        return [words, wordlengths, stems, sentencelengths, punct ]

def compareTextWithTwoModels(newmodel, model1, model2):
    """ compares dictionaries in newmodel with corresponding normalized dictionaries
        in model1 adn model2, printing comparisons of log-probabilities 
        and deciding whether newmodel matches model1 or model2 better
    """
    loglist = []
    for x in range(len(newmodel)):
        loglist.append(compareDictionaries(newmodel[x], model1[x], model2[x]))
    model1win = 0
    model2win = 0
    for x in loglist:
        if x[0]>x[1]:
            model1win += 1
        elif x[0]<x[1]:
            model2win += 1
        else:
            pass
    print("Model 1 wins ", model1win, "times.")
    print("Model 2 wins ", model2win, "times.")
    if model1win>model2win:
        print("Model 1 is a more accurate representation of the test text.")
    elif model2win>model1win:
        print("Model 2 is a more accurate representation of the test text.")
    else:
        print("This test is inconclusive.")
