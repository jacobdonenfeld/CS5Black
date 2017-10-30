import random
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
    key = ["$"]*lengthK
    for i in range(numwords):
        nextL = random.choice(mmodel[tuple(key)])
        print(nextL, end = ' ')
        key = key[1:] + [removePeriod(nextL)]
    return

text = "A B C. A B B C B. A B C C C D B B. B B C C D D B C."
d = (markov_model(text, 2))
print(d)
gen_from_model(d, 10)