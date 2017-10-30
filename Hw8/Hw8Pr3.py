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
    root, yesChild, noChild = tree
    if yesChild == None and noChild == None:
        return True
    return False

def playLeaf(tree):
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
    f1 = open(fileName, "w")  # Open file bar.txt for writing
    f1.write(saveTreeHelper(tree)) # Add \n afer each food to put on its own line
    f1.close()  # close the file

def saveTreeHelper(tree):
    root, yesChild, noChild = tree
    if leaf(tree):
       return root + "\nLeaf\n"
    if tree == None: return ""
    return root + "\nInternal node\n" + saveTreeHelper(yesChild) + saveTreeHelper(noChild)
newtree = ('Is it bigger than a breadbox?', ('an elephant', None, None), ('a mouse', None, None))
#saveTree(newtree, "tree2.txt")
# def buildTreeHelper(treeList):
#
# def buildTree(fileName):
#     fileHandle = open(fileName, "r")
#     list1 = fileHandle.readlines()
#     fileHandle.close()
#     cleanList1 = list(map(lambda x: x.strip("\n"), list1))
#     tree1 = buildTreeHelper(cleanList1)
#     print(list1)
#     return
# buildTree(tree2.txt)
def playLoop(tree):
    play(tree)


def main():
    print("Welcome to binary tree guessing game")
    tree = ("Is it bigger than a breadbox?", ("an elephant", None, None), ("a mouse", None, None))
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