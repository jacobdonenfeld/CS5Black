# Starter file for Hmmmwork6, updated for python3
# hw6 problem 3
#
# date: 
#
# Hmmm...
#
#

# These statements are to set up Hmmm...
# You'll need the files that are in this folder.
import importlib
import hmmmAssembler ; importlib.reload(hmmmAssembler)
import hmmmSimulator ; importlib.reload(hmmmSimulator)
import sys

# For cs5gold, you'll write a fibonacci program
# For cs5black, it's a recursive Hanoi-solving program

# Either way, be sure to call it Problem3 !

# This is a placeholder by that name whose code you'll replace:
Problem3 = """
0	setn r15 100	#set pointer to 100	
1	read r1	# of disks	
2	read r2	# starting peg	
3	read r3	# destination peg	
4	calln r14 6	#calls func on 7	
5	halt	#halts func	
6	copy r4 r1		#modify r1 in r4
7	addn r4 -1		#jump to storer r1
8	nop		
9	jnezn r4 14	#check if r1 != 0	
10	nop		#nopnop
11	write r2	#write r2	
12	write r3	#write r3	
13	jumpr r14	#return back to main	
14	nop		#nop
15	setn r6 6	#store numb disks	
16	sub r6 r6 r2	#move stack	
17	sub r6 r6 r3	#store numb disks	
18	storer r1 r15	#store numb disks	
19	addn r15 1	#move stack	
20	storer r2 r15	#store starting peg	
21	addn r15 1	#move stack	
22	storer r3 r15	#store dest peg	
23	addn r15 1	#add stack up	
24	storer r6 r15	#store r6 on stack	
25	addn r15 1	#move stack again yay	
26	storer r14 r15	#gotta store r14 too 	
27	addn r15 1	#add stack up	
28	nop	#nop	noppitynop
29	addn r1 -1	#r1 is smaller by uno	
30	copy r3 r6	#move r6 over ther 	
31	calln r14 6	#**call tower func	
32	addn r15 -1		#stack down
33	loadr r14 r15		#load r14
34	addn r15 -1		#stack down
35	loadr r6 r15	#load r6	
36	addn r15 -1	#lower stack	
37	loadr r3 r15	#load dest peg on r3	
38	addn r15 -1	#lower stack	
39	loadr r2 r15	#load start peg on r2	
40	addn r15 -1	#lower stack	
41	loadr r1 r15	#load disk numb on r1	
42	storer r1 r15	#store numb disks	
43	addn r15 1	#move stack	
44	storer r2 r15	#store starting peg	
45	addn r15 1	#move stack	
46	storer r3 r15	#store dest peg	
47	addn r15 1	#add stack up	
48	storer r6 r15	#store r6 on stack	
49	addn r15 1	#move stack again yay	
50	storer r14 r15	#gotta store r14 too 	
51	addn r15 1	#add stack up	
52	nop		
53	nop		#nopp
54	nop		
55	nop		#ponnop
56	setn r1 1	#r1 is now 1	
57	nop
58	calln r14 6	#**call tower func	
59	addn r15 -1		#stack down
60	loadr r14 r15		#load r14
61	addn r15 -1		#stackdown
62	loadr r6 r15	#load r6	
63	addn r15 -1	#lower stack	
64	loadr r3 r15	#load dest peg on r3	
65	addn r15 -1	#lower stack	
66	loadr r2 r15	#load start peg on r2	
67	addn r15 -1	#lower stack	
68	loadr r1 r15	#load disk numb on r1	
69	storer r1 r15	#store numb disks	
70	addn r15 1	#move stack	
71	storer r2 r15	#store starting peg	
72	addn r15 1	#move stack	
73	storer r3 r15	#store dest peg	
74	addn r15 1	#add stack up	
75	storer r6 r15	#store r6 on stack	
76	addn r15 1	#move stack again yay	
77	storer r14 r15	#gotta store r14 too 	
78	addn r15 1	#add stack up	
79	nop		
80	nop		
81	nop		
82	nop		
83	addn r1 -1	#r1 is smaller by 1	
84	copy r2 r6	#move r6 over ther 	
85	calln r14 6	#**call tower func	
86	addn r15 -1		#stackdown
87	loadr r14 r15		#load r14
88	addn r15 -1		#stack down
89	loadr r6 r15	#load r6	
90	addn r15 -1	#lower stack	
91	loadr r3 r15	#load dest peg on r3	
92	addn r15 -1	#lower stack	
93	loadr r2 r15	#load start peg on r2	
94	addn r15 -1	#lower stack	
95	loadr r1 r15	#load disk numb on r1	
96	jumpr r14		#jump back to beginning r14
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
