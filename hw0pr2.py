from functools import reduce
import math
def inverse(n):
    return 1/n

def add2(x, y):
    return x + y

def e(n):
    list2 = map(inverse, map(factorial, range(1,n+1)))
    return reduce(add2, list2) + 1
def error(n):
    return math.e - e(n)
def multi(x, y):
    return x * y
def factorial(n):
    return reduce(multi, range(1,n+1))
def mean(L):
    hold = reduce(add2, L)
    return hold/len(L)
def divides(n):
    def div(k):
        return n % k == 0
    return div
def prime(n):
    d = divides(n)
    x = (list(map(d, range(2,n))))
    return not any(x)
