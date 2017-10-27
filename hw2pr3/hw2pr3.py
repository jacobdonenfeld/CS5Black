#GT-A-CGTCGATAACTG-
#-TGATCGTC-ATAAC-GT
def fancyLCS(S1, S2):
    """Returns the length of the longest common subsequence of S1 and S1."""
    if S1 == "" or S2 == "":
        return [0, "", ""]
    else:
        if S1[0] == S2[0]:                 # Match...
            gift =  fancyLCS(S1[1:], S2[1:])
            return [gift[0] + 1, S1[0] + gift[1], S2[0] + gift[2]]# ... so we get 1 match point and then recurse
        else:                               # No match...
           option1 = fancyLCS(S1, S2[1:])
           option2 = fancyLCS(S1[1:], S2)
           if option1[0] == option2[0]:
               return [option1[0], option1[1]+ "#", option2[2] + "#"]
           if option1[0] > option2[0]:
               return [option1[0], option1[1], option2[2] + "#"]
           else:
               return [option2[0], option1[1]+ "#", option2[2]]

def align(S1, S2):
    """Returns the length of the longest common subsequence of S1 and S1."""
    if S1 == "":
        return [0, "-" * len(S2), S2]
    if S2 == "":
        return [0, S1, "-" * len(S1)]
    else:
        if S1[0] == S2[0]:                 # Match...
            gift =  align(S1[1:], S2[1:])
            return [gift[0] + 1, S1[0] + gift[1], S2[0] + gift[2]]# ... so we get 1 match point and then recurse
        else:                               # No match...
           option1 = align(S1, S2[1:])
           option2 = align(S1[1:], S2)

           if option1[0] > option2[0]:
               return [option1[0], "-" + option1[1], S2[0] + option1[2]]
           else:
               return [option2[0], S1[0] + option2[1], "-" + option2[2]]
for i in range(5,len(RNA)):
