import random
from Board import *
class Player:

    def __init__(self, ox, tbt, ply):
        self.ox = ox
        self.tbt = tbt.lower()
        self.ply = ply
        self.symbol = ox

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
        if b.winsFor(self.ox):
            return [100.0 for x in range(b.width)]
        elif b.winsFor(self.oppChar()):
            return [100.0 for x in range(b.width)]
        for x in range(b.width):
            if not b.allowsMove(x):
                scores[x] = -1.0
        if self.ply == 0:
            for x in range(b.width):
                b.addMove(x, self.ox)
                scores[x] = self.scoreBoard(b)
                b.delMove(x)
            return scores
        else:
            for col in range(b.width):
                scores[col] = self.baseCase(b, col)
            for col in range(b.width):
                b.addMove(col, self.ox)
                opp = Player(self.oppChar(), "Random", ply-1)
                x = 100 - max(opp.scoresFor(b))
                b.delMove(col)
            return scores.index(max(scores))






    def nextMove(self, b):
        """ Takes a board as input and returns the next move for this player
            where a move is a column in which the player should place its
            game piece. """


b = Board(7,6)
b.setBoard( '1211244445' )
Player('X', 'LEFT', 0).scoresFor(b)
