import random
from Board import *
class Player:

    def __init__(self, ox, tbt, ply):
        self.ox = ox
        self.tbt = tbt.lower()
        self.ply = ply

    def __repr__(self):
        output = ""
        output += "Player for "+self.symbol+"\n"
        output += "  with tiebreak: " + self.tieRule+"\n"
        output += "  and ply == " + str(self.ply)+"\n"
        return output
    
    def oppChar(self):
        """ Return the opposite game piece character. """
        if self.symbol == "O": return "X"
        else: return "O"

    def scoreBoard(self, b):
        """ Return the score for the given board b."""
        if b.winsFor(self.ox):
            return 100.0
        if b.winsFor(self.oppChar()):
            return 0.0
        return 50.0


    def tiebreakMove(self, scores):
        """ Return column number of move based on self.tbt. """
        check = 0
        maxindex = []
        max = 0
        for x in range(len(scores)):
            if scores[x] > max:
                max = scores[x]
                maxindex = [x]
            if scores[x] == max:
                maxindex.append(x)
        if self.tbt == "left":
            return maxindex[0]
        if self.tbt == "right":
            return maxindex[-1]
        else:
            return maxindex[random.randrange(0,len(maxindex))]

    def scoresFor(self, b):
        """ Return a list of scores for board d, one score for each column
            of the board. """
        scores = [50.0 for x in range(b.width)]
        for col in range(b.width):
            scores[col] = self.baseCase(b, col)
        for col in range(b.width):
            b.addMove(self.ox)
            boards = [Board(b.width, b.height) for x in b.width]
            opp = Player(self.oppChar(), "Random", ply-1)
            for x in range(len(b.width)):
                boards[x].addMove(x)
            scores[col] = max(self.scoresFor(b)) - max(list(map(opp.scoresFor(), boards)))
        return scores.index(max(scores))


            return self.baseCase(b, col)

    def baseCase(self, b, col):
        if not b.allowsMove(col):
            return -1.0
        if b.winsFor(self.ox):
            return 100.0
        if b.winsFor(self.oppChar()):
            return 0.0
        if self.ply == 0:
            return self.scoreBoard(b)
        return "hi"
        #TODO negate return




    def nextMove(self, b):
        """ Takes a board as input and returns the next move for this player
            where a move is a column in which the player should place its
            game piece. """


b = Board(7,6)
b.setBoard( '1211244445' )
Player('X', 'LEFT', 0).scoresFor(b)
