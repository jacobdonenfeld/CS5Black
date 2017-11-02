# Starter file for Hmmmwork6, updated for python3
# hw6 problem 4
#Names: Ethan, Jacob
# date: Oct 21
#
#
from functools import *

def nimSum(piles):
    '''returns the nim sum of the piles'''
    return reduce(lambda x,y: x ^ y, piles)

def computerTakes(piles):
    '''takes a list of piles and returns a list with the best move outlined by pile at index 0, and number to take at index 1'''
    for i in range(len(piles)):
        x = 0
        while (piles[i] - x) != 0:
            x += 1
            test = piles[:i] + [piles[i] - x] + piles[i+1:]
            if nimSum(test) == 0:
                return (i, x)
    for i in range(len(piles)):
        if piles[i] != 0:
            return (i, 1)

def main():
    '''interactive game of nim!'''
    pilecount = []
    while True:
        userInput = (input("How many piles do you want hmmm? "))
        try:
            piles = int(userInput)
            assert(piles > 0)
        except (ValueError, AssertionError):
            print("Only positive ints, bro ")
            continue

        break
    for i in range(piles):
        while True:
            userInput = (input("How many coins in pile " + str(i+1) + " "))
            try:
                count = int(userInput)
                assert (count > 0)
            except (ValueError, AssertionError):
                print("Only positive ints, bro ")
                continue
            pilecount.append(int(count))
            break
    print(pilecount)
    while sum(pilecount) != 0:
        pileMove = (computerTakes(pilecount))[0]
        Takeaway = (computerTakes(pilecount))[1]
        pilecount = pilecount[:pileMove] + [pilecount[pileMove] - Takeaway] + pilecount[pileMove+1:]
        print("Computer removes " + str(Takeaway) + " from pile " + str(pileMove + 1))
        print("Board is now " + str(pilecount))
        if sum(pilecount) == 0:
            print("Computer Wins! ")
            break
        while True:
            userInput = input("Your Turn. Which pile would you like to remove from?")
            try:
                pileMove = int(userInput)-1
                assert (pileMove < piles and pileMove >= 0)
            except (ValueError, AssertionError):
                print("Out of range!")
                continue
            break
        while True:
            userInput = input("Your Turn. How many coins would you like to remove? ")
            try:
                Takeaway = int(userInput)
                assert (Takeaway <= pilecount[pileMove] and Takeaway > 0)
            except (ValueError, AssertionError):
                print("Out of range! ")
                continue
            break
        pilecount = pilecount[:pileMove] + [pilecount[pileMove] - Takeaway] + pilecount[pileMove + 1:]
        print(pilecount)
        if sum(pilecount) == 0:
            print("Human Wins! ")
            break

