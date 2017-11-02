# Starter file for Hmmmwork6, updated for python3
# hw6 problem 2
#
# name(s): Jacob And Ethan
# date: 10/21
#
#
#

# These statements are to set up Hmmm...
# You'll need the files that are in this folder.
import importlib
import hmmmAssembler ; importlib.reload(hmmmAssembler)
import hmmmSimulator ; importlib.reload(hmmmSimulator)
import sys

# For cs5gold, you'll write a power program
# For cs5black, it's a fibonacci program

# Either way, be sure to call it Problem2 !

# This is a placeholder by that name whose code you'll replace:
Problem2 = """
    0	read r1     #input
    1   setn r8 1   #set r8 = 1
    2   write r8    #write first fib number
    3	setn r2 1	#base case set
    4	copy r3 r1  #set r3 = n
    5	addn r3 -1  #decrement r3
    6	jeqzn r3 13 #if at base case, die
    7	add r5 r2 r4 #r5 = r2 + r4
    8	copy r4 r2  #r4 = r2
    9	copy r2 r5  #r2 = r5 = r2 + r4
    10  addn r1 -1  #decrement r1
    11	write r2    #print r2
    12	jumpn 4     #loop
    13  halt    #HAAALT
"""



# This function runs the Hmmm program specified by prog
#
def Hmmm(prog):
    """ This funtion, named Hmmm, takes in a triple-quoted Python string,
        named prog. That string, prog, should be a Hmmm program.

        See the docstring in hw6pr1.py for a full explanation!
    """
    importlib.reload(hmmmAssembler)  # make sure we're using the latest version
    importlib.reload(hmmmSimulator)  # for both assembler and simulator
    fail = hmmmAssembler.main(prog)  # assemble input into machine code
    if fail is None:
        hmmmSimulator.main(['-n'])   # run that code, don't ask for debugging...
