from math import *
def change(amount, coins):
    """amount is change to be made, coins is a list of possible coins"""
    if amount == 0: return 0
    if amount < 0: return inf
    elif coins == []: return inf
    useIt = 1 + change(amount - coins[0], coins)
    loseIt = change(amount, coins[1:])
    return min(useIt, loseIt)



def giveChange(amount, coins):
    if amount == 0: return [0, []]
    elif amount < 0: return [inf, []]
    elif coins == []: return [inf, []]
    gift = changeHelper(amount - coins[0], coins)
    useIt = [gift[0] + 1, [coins[0]] + gift[1]]
    loseIt = changeHelper(amount, coins[1:])
    if useIt[0] > loseIt[0]: return loseIt
    else: return useIt
