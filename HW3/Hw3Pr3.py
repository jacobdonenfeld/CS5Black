from functools import reduce


miniWordList = ["a", "am", "amp", "ample", "as", "asp", "at", "ate", "sat",
                "spa", "spam", "tea", "was", "wasp"]

def wordBreak(string):
    """game to see if you can find more words in dict than the computer"""
    scoreFunction = len  # We're setting the scoring function.  We can change that function to something else!
    wordList = miniWordList  # We're setting the list of valid words.  It can be changed to something else!
    userInput = input("Enter your best solution: ")  # Get user input
    userList = userInput.split() # split the input string into a list of strings
    if check(userList, string, wordList):
        userScore = reduce(lambda X, Y: X+Y, map(scoreFunction, userList))
        print("Your score was ", userScore)
        best = showStringScore(string, scoreFunction, wordList, {})
        print("Best solution is ", best)
    else:
        print("Your solution wasn't valid!")

def  check(playerList, string, wordList):
    """recursively checking string to see if the first word is in it, subtracting it in wordlist, and continuing"""
    if playerList == []:
        return True
    if playerList[0] in wordList:
        if playerList[0] in string:

            newString = string[0:string.index(playerList[0])] + string[len(playerList[0])+string.index(playerList[0]):]
            return check(playerList[1:], newString, wordList)
    else:
        return False

# def stringStore(string, scoreFunction, wordList, memo):
#     if
#     max(list(map(lambda x: stringStore()



