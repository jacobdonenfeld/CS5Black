def play(tree):
    if leaf(tree):
        return playLeaf(tree)
    else:
        root, yesChild, noChild = tree
        answer = input(root + " ").lower()
        if answer == "yes":
            return (root, play(yesChild), noChild)
        else:
            return (root, yesChild, play(noChild))

def leaf(tree):
    if tree == None:
        return True
    root, yesChild, noChild = tree
    if yesChild == None and noChild == None:
        return True
    return False

test
def playLeaf(tree):
    if tree == None:
        return
    root, yesChild, noChild = tree
    answer = input("is it a " + root + " ").lower()
    if answer == "yes":
        print("I got it!")
        return tree
    item = input("Drats! What was it?")
    question = input("Give me a question that distinguishes between a " + root + " and a " + item)
    yesorno = input("Would you answer yes or no for " + item)
    if yesorno == "yes":
        return (question, (item, None, None), (root, None,None))
    elif yesorno == "no":
        return (question, (root, None, None), (item, None, None))

def saveTree(tree, fileName):
    if ".txt" not in fileName:
        fileName += ".txt"
    f1 = open(fileName, "w")  # Open file bar.txt for writing
    f1.write(saveTreeHelper(tree)) # Add \n afer each food to put on its own line
    f1.close()  # close the file

def saveTreeHelper(tree):
    if tree == None: return ""
    root, yesChild, noChild = tree
    if leaf(tree):
       return root + "\nLeaf\n"
    return root + "\nInternal node\n" + saveTreeHelper(yesChild) + saveTreeHelper(noChild)
#newtree = ('Is it bigger than a breadbox?', ('an elephant', None, None), ('a mouse', None, None))

def playLoop(tree):
    return play(tree)

def buildTree(file):
    fileHandle = open(file, "r")  # open up the file for reading
    list1 = fileHandle.readlines()  # read the file into a list
    fileHandle.close()  # always close your file after you're done with it, lest you accidentally damage it.
    cleanList1 = list(map(lambda x: x.strip("\n"), list1))
    x = buildTreeHelper(cleanList1)
    if x[1] != []:
        print("Could not handle " + x[1])
    else:
        print("Loaded without error")
    return x[0]

def buildTreeHelper(list):
    if list[1] == 'Internal node':
        x, y = buildTreeHelper(list[2:])
        z, r = buildTreeHelper(y)
        return (list[0], x, z), r
    elif list[1] == 'Leaf':
        return (list[0], None, None), list[2:]
    else:
        print("None")
print(buildTreeHelper(["Is it bigger than a breadbox?", "Internal node", "an elephant", "Leaf", "a mouse","Leaf"]))

def main():
    print("Welcome to binary tree guessing game")
    tree = ("Is it bigger than a breadbox?", ("an elephant", None, None), ("a mouse", None, None))
    load = input("Would you like to load a previous game?").lower()
    filenamee = "whatever"
    if load == "yes":
        filenamee = input("What is the file name?")
        if ".txt" not in filenamee:
            filenamee += ".txt"
        tree = buildTree(filenamee)
    while True:
        tree = playLoop(tree)
        again = input("Would you like to play again?").lower()
        if again != "yes":
            break
    save = input("Would you like to save your game?")
    if save == "yes":
        filename = input("What would you like to name the file?")
        saveTree(tree, filename)
    print("Thanks for playing!")
main()