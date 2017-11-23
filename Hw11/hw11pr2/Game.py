from Board import *
from Player import *

def main():
    """ Human versus AI game.  No code to write here! """
    k = int(input("Enter ply (level from 0 to 5): "))
    px = "human"
    po = Player("O", "LEFT", k)
    b = Board(7, 6)
    playGame(b, px, po)
    
def playGame(b, px, po):
    """ plays a game of Connect Four
        p1 and p2 are objects of type Player OR
        the string 'human'.
    """
    # Game starts with "X" moving, but this will alternate and thus
    # the nextPieceToMove will alternate during game play, so the
    # nextPieceToMove at the end of the game will be the winner which
    # could be "X" or "O".
    nextPieceToMove = px.ox
    nextPlayerToMove = px

    # FILL IN CODE HERE
    if px == "Human"
        variable = input("what col do you want to place the piece in?")
        b.addMove(nextPieceToMove)
    else: b.addMove(px.nextMove(b))
    if b.winsFor(nextPieceToMove):
        return (b ,nextPieceToMove)
    else:
        return playGame(b, po, px)


    return(b.data, nextPieceToMove)
    
