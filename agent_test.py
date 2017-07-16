"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

#ignore this file - tournament.py will be used for final evaluation
import unittest

import isolation
import game_agent

from importlib import reload

from sample_players import (RandomPlayer, open_move_score,
                            improved_score, center_score)

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)


if __name__ == '__main__':
    print('\n\n\n Sssstarting!')
    unittest.main()
    
    #my:
    from game_agent import *
    from sample_players import *
    from isolation import Board
    
    player1 = AlphaBetaPlayer(score_fn=custom_score_3) #AlphaBetaPlayer() #MinimaxPlayer() #RandomPlayer() #GreedyPlayer
    #"illegal move" is the standard win conditions in sample_players
    player2 = AlphaBetaPlayer(score_fn=improved_score) #
    p1id=id(player1)
    p2id=id(player2)
    print('p1=',id(player1))
    print('p2=',id(player2))
    
#    game = Board(player1, player2)
#    #STARTING LOCATIONS FOR BOTH PLAYERS - REPLACE WITH RANDOM LATER?
#    game.apply_move((2, 3))
#    game.apply_move((0, 5))
#    
#    winner, history, outcome = game.play() #play(self, time_limit=TIME_LIMIT_MILLIS)
#    #player1.minimax(game,3)
#
#    print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
#    print(game.to_string())
#    print("Move history:\n{!s}".format(history))
    
    
    p1wins=0
    p2wins=0

    for i in range(10):

        
        game = Board(player1, player2)
        #STARTING LOCATIONS FOR BOTH PLAYERS - FIXED
        #game.apply_move((2, 3))
        #game.apply_move((0, 5))
        #RANDOM STARTING LOCATIONS
        p1startx=randint(0,6)
        p1starty=randint(0,6)
        game.apply_move((p1startx, p1starty))
        p2startx=randint(0,6)
        p2starty=randint(0,6)
        while ((p1startx==p2startx) and (p1starty==p2starty)):
            p2startx=randint(0,6)
            p2starty=randint(0,6)
        
        winner, history, outcome = game.play()
        print("winner=",str(winner))
        print("outcome=",str(outcome))
        #print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
#        if id(winner) == id(player1):
#            p1wins+=1
#        if id(winner) == id(player2):
#            p2wins+=1
        if winner is player1:
            p1wins+=1
        if winner is player2:
            p2wins+=1
    print("p1 wins =", p1wins)
    print("p2 wins =", p2wins)