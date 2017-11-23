# Connect 4 Game Board

class Board:

    def __init__( self, width=7, height=6 ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        self.data = [[' ']*width for r in range(height)]

    def getWidth():
        return self.width

    def getHeight():
        return self.height

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        s = ''   # the string to return
        for row in range( self.height ):
            s += '|'   # add the spacer character
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += '\n'
        s += '--'*self.width    # add the bottom of the board
        s += '-\n'
        for col in range( self.width ):
            s += ' ' + str(col%10)
        s += '\n'
        return s       # the board is complete, return it

    def addMove(self, col, ox):
        """ Add the game piece ox (either 'X' or 'O') to column col. """
        VariableNameNumberOne = len(self.data)
        for i in range(VariableNameNumberOne):
            if self.data[VariableNameNumberOne - 1 - i][col] == " ":
                self.data[VariableNameNumberOne - 1 - i][col] = ox
                break


    def clear(self):
        """ Clear the game board of all game pieces. """
        #TODO ask Ran if I can create a new board obj and set the pointer previously used to it
        self.data = [[' '] * width for r in range(height)]

    def setBoard(self, moves):
        """ Set the board using an input string representation. """
        #0 = x, 1 = o
        toggle = 0
        for i in range(len(moves)):
            if toggle == 0:
                self.addMove(int(moves[i]), "X")
                toggle = 1
            else:
                self.addMove(int(moves[i]), "O")
                toggle = 0


    def allowsMove(self, col):
        """ Return True if adding a game piece in the given column is 
            permitted and return False otherwise. """
        if self.data[0][col] == " ":
            return True
        return False

    def isFull(self):
        """ Return True if the game board is full and False otherwise. """
        for i in self.data[0]:
            if i == " ":
                return False
        return True

    def delMove(self, col):
        """ Delete the topmost game piece from the given column. """
        for i in range(len(self.data)):
            if self.data[i][col] != " ":
                self.data[i][col] = " "


    def winsFor(self, ox):
        """ Return True if the game has been won by player ox where ox
            is either 'X' or 'O'. """
        #TODO figure out why this is still out of range
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] == ox:
                    for u in range(3):
                        if i+u +1 >= self.height:
                            break
                        if self.data[i+u+1][j] != ox:
                            break
                        if u != 2:
                            continue
                        return True
                    for u in range(3):
                        if i-u-1 <= -1:
                            break
                        if self.data[i-u-1][j] != ox:
                            break
                        if u != 2:
                            continue
                        return True
                    for u in range(3):
                        if j+u+1 >= self.width:
                            break
                        if self.data[i][j+u+1] != ox:
                            break
                        if u != 2:
                            continue
                        return True
                    for u in range(3):
                        if j-u-1 <= -1:
                            break
                        if self.data[i][j-u-1] != ox:
                            break
                        if u != 2:
                            continue
                        return True
                    #Diagonoals
                    for u in range(3):
                        if i+u+1 >= self.height or j+u+1 >= self.width:
                            break
                        if self.data[i+u+1][j+u+1] != ox:
                            break
                        if u != 2:
                            continue
                        return True
                    for u in range(3):
                        if i-u-1 <= -1 or j-u-1 <= -1:
                            break
                        if self.data[i-u-1][j-u-1] != ox:
                            break
                        if u != 2:
                            continue
                        return True
                    for u in range(3):
                        if i-u-1 <= -1 or j+u+1 >= self.width:
                            break
                        if self.data[i-u-1][j+u+1] != ox:
                            break
                        if u != 2:
                            continue
                        return True
                    for u in range(3):
                        if i+u+1 >= self.height or j-u-1 <= -1:
                            break
                        if self.data[i+u+1][j-u-1] != ox:
                            break
                        if u != 2:
                            continue
                        return True
        return False



