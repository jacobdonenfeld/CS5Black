def complement(base1,base2):
    """Returns boolean indicating if two RNA bases are complementary."""
    if base1=="A" and base2=="U":
        return True
    elif base1=="U" and base2=="A":
        return True
    elif base1=="C" and base2=="G":
        return True
    elif base1=="G" and base2=="C":
        return True
    else:
        return False

def fold(RNA):
    """boolList = Turns RNA into true and false for matches with RNA[0]
    indexList turns boolList into a list with indexes where true
    filledList turns indexList into a list of lists where fList[0]
    is from 0-true, fList[1] is from true to end of RNA"""
    if RNA == "":
        return 0
    if len(RNA) == 1:
        return 0
    if len(RNA) == 2 & complement(RNA[0],RNA[1]):
        return 1
    if len(RNA) == 2 & complement(RNA[0], RNA[1]) == False:
        return 0
    filledList = list(map(lambda x: [RNA[1:x], RNA[x+1:]], filter(lambda x: complement(RNA[0],RNA[x]), range(len(RNA)-1))))
    print(filledList)
    useIt = max(1 + max(list(map(fold, map(lambda x: filledList[x][0], range(len(filledList)-1)))), default=0), default=0) + max(list(map(fold, map(lambda x: filledList[x][1], range(len(filledList)-1))), default=0))
    loseIt = 0 + (max(fold(RNA[1:]), default=0))
    return max(useIt, loseIt, default=0)

print(fold("ACUGAGCCCU"))
