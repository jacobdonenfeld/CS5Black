import time
#worked with Daniel Torres
def fastED(first, second, memo):
    '''Returns the edit distance between the strings first and second.'''
    if (first, second) in memo:
        return memo[(first, second)]
    if first == '':
        return len(second)
    elif second == '':
        return len(first)
    elif first[0] == second[0]:
        memo[(first, second)] = fastED(first[1:], second[1:], memo)
        return memo[(first, second)]
    else:
        substitution = 1 + fastED(first[1:], second[1:], memo)
        deletion = 1 + fastED(first[1:], second, memo)
        insertion = 1 + fastED(first, second[1:], memo)
        memo[(first, second)] = min(substitution, deletion, insertion)
        return memo[(first, second)]

def topNmatches(word,nummatches,ListOfWords):
    distance = list(map(lambda x: [fastED(word, x, {}), x], ListOfWords))
    distance.sort()
    distance = list(map(lambda x: distance[x][1], range(len(distance))))
    return distance[:nummatches]

def spam():
    """ docstring """
    f = open("3esl.txt")
    contents = f.read()
    words = contents.split("\n")
    userInput = input("spell check> ")
    if userInput in words:
        return "Correct"
    else:
        start = time.time()
        x= topNmatches(userInput, 10, words)
        print("Suggested Alternatives")
        for i in range(len(x)):
            print(x[i])
        print("The elapsed time executing spam() was", time.time() - start, "seconds")
