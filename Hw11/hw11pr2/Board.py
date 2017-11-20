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

    def clear(self):
        """ Clear the game board of all game pieces. """

    def setBoard(self, moves):
        """ Set the board using an input string representation. """

    def allowsMove(self, col):
        """ Return True if adding a game piece in the given column is 
            permitted and return False otherwise. """

    def isFull(self):
        """ Return True if the game board is full and False otherwise. """

    def delMove(self, col):
        """ Delete the topmost game piece from the given column. """

    def winsFor(self, ox):
        """ Return True if the game has been won by player ox where ox
            is either 'X' or 'O'. """


