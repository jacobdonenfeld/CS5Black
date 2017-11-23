import random
import sys
sys.setrecursionlimit(99999)
def dollarify(wordlist, k):
    if type(wordlist) == str:
        wordlist = wordlist.split()
    return ["$"]*k + dollarifyHelper(wordlist, k)

def dollarifyHelper(wordlist, k):
    if type(wordlist) == str:
        wordlist = wordlist.split()
        print(wordlist)
    if len(wordlist) == 0:
        return []
    if wordlist[0][-1] == "." or wordlist[0][-1] == "?" or wordlist[0][-1] == "!":
        return [wordlist[0]] + ["$"]*k + dollarifyHelper(wordlist[1:], k)
    return [wordlist[0]] + dollarifyHelper(wordlist[1:], k)

def removePeriod(letter):
    PUNCTUATION = [".", "!", "?"]
    if letter[-1] in PUNCTUATION:
        letter = letter[0:-1]
    return letter

def ending(strr):
    PUNCTUATION = [".", "!", "?"]
    if strr[-1] in PUNCTUATION:
        return True
    return False

def markov_model(wordList, k):
    dict = {}
    if type(wordList) == str:
        wordList = wordList.split()
    wordList = dollarify(wordList, k)
    for i in range(len(wordList)-k):
        if tuple(wordList[i:i+k]) in dict:
            if wordList[i+k] != "$":
                dict[tuple(wordList[i:i+k])] = [wordList[i+k]] + dict[tuple(wordList[i:i+k])]
                continue
        elif wordList[i+k] != "$":
            dict[tuple(wordList[i:i+k])] = [wordList[i+k]]
    return dict

def gen_from_model(mmodel, numwords):
    write = ""
    lengthK = 0
    for k in mmodel:
        lengthK = len(k)
        break
    keyhold = ["$"]*lengthK
    key = keyhold
    for i in range(numwords):
        nextL = random.choice(mmodel[tuple(key)])
        print(nextL, end = ' ')
        if ending(nextL):
            key = keyhold
        else:
            key = key[1:] + [nextL]
    return

def markov(fileName, k, length):
    f1 = open(fileName, "r", encoding="utf8")  # Open text file for reading
    text = f1.read()  # Read the entire contents of the file into a string
    f1.close()
    dol = dollarify(text, k)
    mm = markov_model(dol, k)
    print(gen_from_model(mm, length))

markov("Draft.txt", 2, 5000)