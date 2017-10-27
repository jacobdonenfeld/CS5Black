from functools import *

def numToBaseB(n, B):
    """Converts base 10 into base B"""
    if n == 0:
        return ''
    reman = n % B
    return numToBaseB(n//B, B) + str(reman) #fits even

def baseBToNum(S,B):
    """accepts a string S and a base B, returns int base 10"""
    if len(S) == 1: return int(S)
    return B*baseBToNum(S[:-1],B) + int(S[-1])

def baseToBase(B1,B2,SinB1):
    """converts between two bases"""
    return numToBaseB(baseBToNum(SinB1, B1), B2)
def add(S, T):
    """accepts two binary strings S and T as arguments, and returns their sum, also in binary."""
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)

def letterToUnicode(n):
    """Convert let. to unicode with len = 8"""
    n = numToBaseB(ord(n),2)
    return str((8-len(n))*"0")+n

def charXor(c1,c2):
    """Xors char"""
    if c1 == c2: return 0
    else: return 1
def stringxor(S1,S2):
    """Takes in strings of binary and xors"""
    return reduce(lambda x, y: str(x) + str(y), list(map(lambda x: charXor(S1[x],S2[x]),range(len(S1)))))

def xorStrings(S1,S2):
    """Convert string into unicode, into binary, xor, convert back to char"""
    S1, S2 = [list(map(lambda x: letterToUnicode(S1[x]), range(len(S1)))), list(map(lambda x: letterToUnicode(S2[x]), range(len(S2))))]
    xorS = list(map(lambda x: stringxor(S1[x],S2[x]),range(len(S1))))
    return reduce(lambda x, y: str(x) + str(y), list(map(lambda x: chr(baseBToNum(x, 2)), xorS)))

print(xorStrings("spam", "zng!"))
encripted = xorStrings("spam", "zng!")
print(xorStrings(encripted,"zng!"))