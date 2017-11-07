import math
import itertools
def compress():
    x = input("Enter name of file to compress")
    string = read_String(x)
    occur = occurances(string)
    tree = build_tree(occur)
    bindict = build_dict(tree, occur)
    binarystring = sequence_str(string, bindict)
    binarylist = seq_to_ByteList(binarystring)
    numblist = bytel_to_numbl(binarylist)
    write_Bites(numblist, x + ".HUFFMAN")
    write_String(str(bindict) + str(len(binarystring) % 8), x + ".HUFFMAN.KEY")

def write_String(string, filename):
    f2 = open(filename, "w")  # Open text file for writing
    f2.write(str(string))  # write each character followed by a newline
    f2.close()

def read_String(filename):
    f1 = open(filename, "r")  # Open text file for reading
    text = f1.read()  # Read the entire contents of the file into a string
    f1.close() # Always close files after opening them!
    print("I just read in ", text)
    return text

def write_Bites(bytelist,filename):
    f3 = open(filename, "wb")
    f3.write(bytes(bytelist))  # Convert numbers to bytes and write out!
    f3.close()

def BinaryToNum(string):
    answer = 0
    for x in string:
        answer = answer * 2
        if x == "1":
            answer = answer + 1
    return answer

def bytel_to_numbl(bytelist):
    return list(map(BinaryToNum, bytelist))

def occurances(string):
    dict = {}
    total = len(string)
    for i in range(total):
        if string[i] not in dict:
            dict[string[i]] = 1
        else: dict[string[i]] += 1
    for key in dict:
        dict[key] = dict[key] / total
    return dict
def strip_dict(dict):
    return list(dict.keys())

def max_dict(dict):
    return min(dict, key=dict.get)
def min_dict(dict):
    return min(dict, key=dict.get)

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

def build_tree(dict):
    if len(dict) == 1:
        for i in dict:
            return i
    x1 = min_dict(dict)
    y1 = dict[x1]
    dict = removekey(dict, x1)
    x2 = min_dict(dict)
    y2 = dict[x2]
    dict = removekey(dict, x2)
    x3 = (x1, x2)
    y3 = y1 + y2
    dict[x3] = y3
    return build_tree(dict)

def build_dict(tree, dict):
    newDict= {}
    strippedDict = strip_dict(dict)
    for i in strippedDict:
        newDict[i] = helper_dict(tree, i)
    return newDict

def helper_dict(tree, i):
    if type(tree) == str:
        if tree == i:
            return ""
        return "NO"
    elif tree == None:
        return "NO"
    else:
        useIt = "1" + helper_dict(tree[0], i)
        if "NO" not in useIt:
            return useIt
        loseIt = "0" + helper_dict(tree[1], i)
        return loseIt

def sequence_str(string, dict):
    newstr = ""
    for i in range(len(string)):
        newstr += dict[string[i]]
    return newstr

def seq_to_ByteList(string):
    byteList = []
    x = 8 - (len(string)% 8)
    string += "0"*x
    for i in range(0, len(string),8):
        byteList.append(string[i:i+8])
    return byteList

