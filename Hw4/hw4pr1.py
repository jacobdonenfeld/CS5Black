# CS5 Gold/Black, hw4pr1
# Filename: hw4pr1.py
# Name:
# Problem description: Binary <-> decimal conversions

def isOdd(n):
    """checks if N is odd"""
    if n%2 == 0: return False
    return True
def numToBinary(n):
    if n == 0: return ''
    elif n % 2 == 1: return numToBinary(n//2) + '1'
    else: return numToBinary(n//2) + '0'
def binaryToNum(S):
    if S == '': return 0
    elif S[-1] ==  '1': return 2*binaryToNum(S[:-1])+ 1 # if the last digit is a '1'...
    else:  return 2*binaryToNum(S[:-1]) + 0 # last digit must be '0'
def increment(S):
    """Increments binary num S by 1"""
    if S == '11111111': return '00000000'
    n = numToBinary(1+int(binaryToNum(S)))
    return str(0)*(8-len(str(n))) + str(n)
def count(S, n):
    print(S)
    if n == 0: return
    return count(increment(S),n-1)
def numToTernary(n):
    if n == 0: return ''
    elif n % 3 == 2: return numToTernary((n//3)) + '2'
    elif n % 3 == 1: return numToTernary(n//3) + '1'
    else: return numToTernary(n//3) + '0'
def ternaryToNum(S):
    if S == '': return 0
    elif S[-1] ==  '1': return 3*ternaryToNum(S[:-1])+ 1
    elif S[-1] ==  '2': return 3*ternaryToNum(S[:-1])+ 2
    else:  return 3*ternaryToNum(S[:-1]) + 0 # last digit must be '0'
def balancedTernaryToNum(S):
    if S == "":
        return 0
    elif S[-1] == '+': return 3*balancedTernaryToNum((S[:-1])) + 1
    elif S[-1] == '0': return 3*balancedTernaryToNum(S[:-1]) + 0
    elif S[-1] == '-': return 3*balancedTernaryToNum(S[:-1]) -1
    return "You messed up"
def numToBalancedTernary(n):
    """Converts number base 10 into this funky counting thing"""
    if n == 0: return ''
    elif n % 3 == 1: return numToBalancedTernary(n//3) + '+'
    elif n % 3 == 2: return numToBalancedTernary((3+n)//3)+ '-'
    else: return numToBalancedTernary(n//3) + '0'
