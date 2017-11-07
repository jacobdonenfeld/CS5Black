import itertools
import functools
import ast
import sys
sys.setrecursionlimit(10000)
def uncompress():
    while(True):
        x = input("Enter .HUFFMAN file")
        if ".HUFFMAN" in x:
            break
        print("File does not work")
    listofbytes = readbyte(x)
    binstring = list_to_string(listofbytes)
    while(True):
        x = input("Enter .HUFFMAN.KEY file")
        if ".HUFFMAN.KEY" in x:
            break
        print("File does not work")
    a = read_dict(x)
    #lst = a.split()
    lst = find_numb(a)
    print("LST")
    print(lst)
    bindict = ast.literal_eval(lst[0])
    bindict = swap(bindict)
    newbinstr = binstring[0:(len(binstring) - 8 + int(lst[1]))]
    str = make_str(bindict, newbinstr)
    write_String(str, x[:-3]+"DECODED")

def find_numb(string):
    x=0
    while(True):
        if string[-x]== "}":
            return [string[:-(x-1)], string[-(x-1):]]
        x += 1


def make_str(dict, binstring):
    if len(binstring) == 0:
        return ""
    x = 0
    while(True):
        if binstring[0:x] in dict:
            print(dict[binstring[0:x]])
            return dict[binstring[0:x]] + make_str(dict, binstring[x:])
        x += 1


def write_String(string, filename):
    f2 = open(filename, "w")  # Open text file for writing
    f2.write(str(string))  # write each character followed by a newline
    f2.close()


def swap(dict):
    return {v: k for k, v in dict.items()}

def readbyte(filename):
    f4 = open(filename, "rb")
    readBytes = f4.read()
    f4.close()
    return list(readBytes)  # convert bytes to list of numbers

def read_dict(dictname):
    f1 = open(dictname, "r")  # Open text file for reading
    text = f1.read()  # Read the entire contents of the file into a string
    f1.close()  # Always close files after opening them!
    print("I just read in ", text)
    return text

def list_to_string(list):
     stringyay = ""
     for x in range(len(list)):
         stringyay += EightBitNumToBinary(list[x])
     return stringyay

def EightBitNumToBinary(num):
    output = ""
    while num > 0:
        if num % 2 == 0:
            output = "0" + output
        else:
            output = "1" + output
        num = int(num/2)
    padding = 8 - len(output)
    return padding * "0" + output

