# Your name here
# Date
# hw4pr3.py
from itertools import chain
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from functools import *
import numpy as np
#import itertools
# A sample 8x8 image represented as a sequence of 64 bits
test1 = "0000001100001100000000110000001111111111111111111111111111111111"

def powerOfTwo(num):
    """ PROVIDED CODE. """
    """ Takes a positive integer as input and returns True if and only if it is a power of two. """
    if num == 1: return True
    elif num % 2 == 1: return False
    else: return powerOfTwo(num//2)

def pngToArray(filename, threshold=2):
    """ PROVIDED CODE. """
    """ Takes a filename as input, where the file is a .png image, and returns a binary
    2D array as output.  The image must be a square whose dimensions are a power of two. """
    img=mpimg.imread(filename)  # read in the image
    dimensions = img.shape  # Get the dimensions
    rows = dimensions[0]    # Extract the number of rows...
    columns = dimensions[1] # ... and columns
    if rows != columns or not powerOfTwo(rows):  # check if the image is of appropriate dimensions
        return None  
    array = []  # start building the output array
    for r in range(rows):
        row = []
        for c in range(columns):
            if sum(img[r][c]) >= threshold:
                row.append(0)
            else:
                row.append(1)
        array.append(row)
    return array

def renderASCII(array):
    """ PROVIDED CODE. """
    """ Takes a 2D array of 0's and 1's as input and renders it as 0's and 1's on the screen  """
    for row in array:
        stringify = reduce(lambda X, Y: str(X) + str(Y), row)
        print(stringify)
            
def renderImage(array):
    """ PROVIDED CODE. """
    """ Takes a 2D array of 0's and 1's as input and renders it on the screen using matplotlib. """
    dim = len(array)
    image = np.zeros((dim, dim), dtype = np.float)
    for r in range(dim):
        for c in range(dim):
            image[r][c] = float(array[r][c]) 
    plt.imshow(image, cmap="Greys", interpolation='nearest')
    plt.show()
    
def stringToArray(bstring):
    """ PROVIDED CODE. """
    """ Takes a binary string as input and returns the 2D array representation of the image. """
    dim = int(math.sqrt(len(bstring)))
    charArray = [list(bstring[i:i+dim]) for i in range(0, len(bstring), dim)]
    array = [ [int(x) for x in row] for row in charArray ]
    return array

def quadrants(array):
    """ Takes an array of bits as input and returns a list of quadrants
    of the form [NW, NE, SW, SE] where each entry is the array 
    for that quadrant """
    NW = list(map(lambda y: array[y][:len(array[0])//2], range(len(array)//2)))
    NE = list(map(lambda y: array[y][len(array[0])//2:], range(len(array)//2)))
    SW = list(map(lambda y: array[y][:len(array[0])//2], map(lambda x: x+(len(array)//2), range(len(array)//2))))
    SE = list(map(lambda y: array[y][len(array[0])//2:], map(lambda x: x+(len(array)//2), range(len(array)//2))))
    return [NW, NE, SW, SE]

def solidzero(array):
    """ Takes a 2D binary array as input and returns True if every bit is a 0 and False otherwise. """
    # You'll write this code.  One line suffices!
    try: p = reduce(lambda x,y: x + y, map(lambda z: reduce(lambda x, y: x + y, array[z]), range(len(array))))
    except: p = reduce(lambda x,y: x + y, array) #bad code... help
    return p == 0
# print("Zeros?")
# print(solidzero([0, 1, 1, 1, 1, 0, 1, 1]))
def solidone(array):
    """ Takes a 2D binary array as input and returns True if every bit is a 1 and False otherwise. """
    try:
        p = min(map(min, array))
    except:
        p = min(array)
    return p != 0
# print("Ones?")
# print(solidone([1, 1, 1, 1, 1, 1, 1, 1]))
def makeQuadtree(array):
    """ Returns a quadtree representation of the array. """
    if solidone(array):
        return 1
    if solidzero(array):
        return 0
    quadtree = list(map(lambda x: makeQuadtree(x), quadrants(array)))
    return quadtree

def solidArray(value, pixels):
    """ PROVIDED CODE. """
    """ Takes a value (0 or 1) and a number of pixels and retursn a 2D array of picelsxpixels
    bits all of which are set to the given value. """
    return [[value]*pixels for row in range(pixels)]

def makeArray(quadtree, dim):
    """ Takes a quadree and dimension as input and
    returns the 2D array representation of the quadtree """
    if type(quadtree) == int:
        return expandArray(quadtree, dim)
    NW, NE, SE, SW = list(map(lambda x: makeArray(quadtree[x], dim//2), range(4)))
    return compileArray(NW, NE) + compileArray(SE, SW)

def expandArray(intt, dim):
    """Expands array into 2d array with dim*dim"""
    return [[intt]*dim]*dim

def compileArray(array1, array2):
    """Compiles 2 2d arrays into 1 with twice the length of columns. """
    return list(map(lambda x: array1[x]+array2[x], range(len(array1))))
# test1 = '0000001100001100000000110000001111111111111111111111111111111111'
# array1 = stringToArray(test1)
# print("array")
# print(array1)
# print(makeQuadtree(array1))
# print("quadtree")
# print(makeArray([0, [[0, 0, 1, 1], [1, 1, 0, 0], 0, 1], 1, 1], 5))

def rotateRight(quadtree):

    """ Takes a quadtuple as input and returns the quadtree that results when rotating that image
    clockwise 90 degrees."""
    # You'll write this code.  Around four lines of code suffice
    if type(quadtree)== int:
        return quadtree
    return list(map(rotateRight, rotate(quadtree, 1)))
def rotate(list, n):
    return list[-n:] + list[:-n]
def flipHorizontal(quadtree):
    """ Takes a quadtree as input and returns the quadtree that results when flipping the image
    about the horizontal axis of symmetry. """
    # You'll write this code.  Around four lines of code suffice
    
def flipDiagonal(quadtree):
    """ Takes a quadtree as input and returns the quadtree that results when flipping the image
    about the diagonal line through the NE and SW corners of the image. """
    # You'll write this code.  Around four lines of code suffice

def invert(quadtree):
    """ Takes a quadtree as input and returns the quadtree that results when flipping every white
    pixel to a black pixel and vice versa. """
    # You'll write this code.  Around four lines of code suffice
    for x in range(len(quadtree)):
        if type(quadtree[x]) ==(int):
            if quadtree[x] == 1:
                quadtree[x] = 0
            else: quadtree[x] = 1
        else: quadtree[x] = invert(quadtree[x])
    return quadtree
