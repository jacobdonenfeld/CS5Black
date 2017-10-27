# from functools import reduce
def compose(funcList):
    """takes a list of func, returns =f1(f2(f3(... fk(X) ) ) )"""
    print(funcList)
    if len(funcList) == 1: return lambda x: funcList[0](x)
    return lambda x: funcList[0](compose(funcList[1:])(x))

def double(X):
    return 2 * X

def square(X):
    return X ** 2

def makePoly(coeffList):
    return lambda x: coeffList[0] * x ** 2 + coeffList[1] * x + coeffList[2]

