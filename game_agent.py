"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import math
#tourney: Only the following libraries will be allowed: itertools, math, heapq, collections, array, copy, random, numpy, scipy, and scikit-learn (sklearn).

from random import randint #temp
class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass

def custom_score_test(game, player): 
    """Calculate the heuristic value of a game state from the point of view
    of the given player.
    ----------
    Description:
    Weighted "my_moves - opponent_moves" that includes the quality of each move (how close to the center they are)
    Move to the center cell (3,3) is worth 6 points. Anything else is 6 minus L1 distance from the center. Worst move (corner) is 6-3-3=0 points
    ----------
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).
    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)
    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    

    player_moves=game.get_legal_moves(player)
    oppo_moves=game.get_legal_moves(game.get_opponent(player))
    player_move_score=sum([6-abs(move[0]-3) - abs(move[1]-3) for move in player_moves])
    oppo_move_score=sum([6-abs(move[0]-3) - abs(move[1]-3) for move in oppo_moves])
    try:
        return math.log(player_move_score/oppo_move_score)
    except:
        return player_move_score - 1.5*oppo_move_score
#                             Playing Matches                              
#                        *************************                         
#
# Match #   Opponent      Random       Random2      Random3     AB_Custom  
#                        Won | Lost   Won | Lost   Won | Lost   Won | Lost 
#    1       Random      17  |  23    21  |  19    18  |  22    38  |   2  
#    2       MM_Open      8  |  32     4  |  36    10  |  30    27  |  13  
#    3      MM_Center     9  |  31    12  |  28    10  |  30    38  |   2  
#    4     MM_Improved    2  |  38     4  |  36     0  |  40    26  |  14  
#    5       AB_Open      5  |  35     3  |  37     4  |  36    16  |  24  
#    6      AB_Center     1  |  39     3  |  37     3  |  37    25  |  15  
#    7     AB_Improved    1  |  39     2  |  38     2  |  38    21  |  19  
#--------------------------------------------------------------------------
#           Win Rate:      15.4%        17.5%        16.8%        68.2%    
#
#
#Your ID search forfeited 3.0 games while there were still legal moves available to play.
    #return math.log(player_move_score/oppo_move_score) #player_move_score - 1.5*oppo_move_score

def custom_score(game, player): 
    """Calculate the heuristic value of a game state from the point of view
    of the given player.
    ----------
    Description:
    Weighted "my_moves - opponent_moves" that includes the quality of each move (how close to the center they are)
    Move to the center cell (3,3) is worth 6 points. Anything else is 6 minus L1 distance from the center. Worst move (corner) is 6-3-3=0 points
    ----------
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).
    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)
    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    

    player_moves=game.get_legal_moves(player)
    oppo_moves=game.get_legal_moves(game.get_opponent(player))
    player_move_score=sum([6-abs(move[0]-3) - abs(move[1]-3) for move in player_moves])
    oppo_move_score=sum([6-abs(move[0]-3) - abs(move[1]-3) for move in oppo_moves])
        
    return player_move_score - 1.5*oppo_move_score



def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.
    ----------
    Description:
    Calculates how close on average are player and/or the opponent to the unvisited cells on the board. Can use either L1 distance or L2 distance.
    ----------
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).
    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)
    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """    

    def dist_func(pos0,pos1,pos2): #locations of empty cell, player, and opponent respectively
        return abs(pos1[0] - pos0[0]) + abs(pos1[1] - pos0[1]) - abs(pos2[0] - pos0[0]) - abs(pos2[1] - pos0[1]) #difference between player's and opponent's L1 distances

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    player_loc=game.get_player_location(player)
    empty_spaces=game.get_blank_spaces()

    oppo_loc=game.get_player_location(game.get_opponent(player))
    distances=[dist_func(pos0, player_loc, oppo_loc) for pos0 in empty_spaces]
    average_dist=sum(distances)/len(distances)

    return -average_dist #with minus, low abs value is good

def custom_score_3(game, player): 
    """Calculate the heuristic value of a game state from the point of view
    of the given player.
    ----------
    Description:
    Uses fast heuristic early on in the game and more resource consuming one later
    ----------
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).
    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)
    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    def dist_func(pos0,pos1,pos2): #empty, player, opponent locations
        return abs(pos1[0] - pos0[0]) + abs(pos1[1] - pos0[1]) - abs(pos2[0] - pos0[0]) - abs(pos2[1] - pos0[1])
    
    if len(game.get_blank_spaces())>20: #20 remaining empty places is our arbitrary threshold dividing early game and late game
        player_moves=game.get_legal_moves(player)
        oppo_moves=game.get_legal_moves(game.get_opponent(player))
        player_move_score=sum([6-abs(move[0]-3) - abs(move[1]-3) for move in player_moves])
        oppo_move_score=sum([6-abs(move[0]-3) - abs(move[1]-3) for move in oppo_moves])
        return player_move_score - 1.5*oppo_move_score
    else:     
        player_loc=game.get_player_location(player)
        empty_spaces=game.get_blank_spaces()   
        oppo_loc=game.get_player_location(game.get_opponent(player))
        distances=[dist_func(pos0, player_loc, oppo_loc) for pos0 in empty_spaces]
        average_dist=sum(distances)/len(distances)
        return -average_dist


def custom_score_4(game, player): # 
    """Calculate the heuristic value of a game state from the point of view
    of the given player.
    ----------
    Description:
    Uses fast heuristic early on in the game and more resource consuming one later
    ----------
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).
    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)
    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # weighted difference in number of moves. weights picked manually through trial and error.
    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    player_moves_tot = len(game.get_legal_moves(player))
    opponent_moves_tot = len(game.get_legal_moves(game.get_opponent(player)))
    
    return float(player_moves_tot - 1.5*opponent_moves_tot)


def custom_score_5(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.
    ----------
    Description:
    Chases your opponent around. Uses L1 distance
    ----------
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).
    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)
    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    player_loc=game.get_player_location(player)
    oppo_loc=game.get_player_location(game.get_opponent(player))
    return -(player_loc[0] - oppo_loc[0] + player_loc[1] - oppo_loc[1]) 

class IsolationPlayer: 
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.
    ********************  DO NOT MODIFY THIS CLASS  ********************
    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)
    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.
    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
    #def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        #self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left): #GOOD
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.
        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************
        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.
        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).
        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.
        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.
        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md
        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************
        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state
        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting
        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves
        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.
            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """

        if game.active_player == self: #maximizing player
            return self.max_value(game, depth)[1]
        else:
            return self.min_value(game, depth)[1]

    def max_value(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0:
            return self.score(game, self), (-1, -1)

        best_score = float("-inf")
        legal_moves = game.get_legal_moves(self)
        if len(legal_moves)>0:
            best_move = legal_moves[randint(0,len(legal_moves)-1)]
        else:
            best_move= (-1,-1)
        for move in legal_moves:
            next_score, _ = self.min_value(game.forecast_move(move), depth-1)
            if best_score < next_score:
                best_score = next_score
                best_move = move
        return best_score, best_move

    def min_value(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0:
            return self.score(game, self), (-1, -1)

        best_score = float("inf")
        legal_moves = game.get_legal_moves(game.get_opponent(self))
        if len(legal_moves)>0:
            best_move = legal_moves[randint(0,len(legal_moves)-1)]
        else:
            best_move= (-1,-1)
        for move in legal_moves:
            next_score, _ = self.max_value(game.forecast_move(move), depth-1)
            if best_score > next_score:
                best_score = next_score
                best_move = move
        return best_score, best_move

        
class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left): 
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.
        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.
        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************
        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).
        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.
        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        best_move= (-1,-1)
        
        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            
            current_depth = 1
            while True:
                best_move = self.alphabeta(game, current_depth) #use default alpha & beta
                current_depth += 1
                
        except SearchTimeout:
            pass
           # pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
    
        return best_move 
    
    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")): 
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.
        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md
        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************
        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state
        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting
        alpha : float
            Alpha limits the lower bound of search on minimizing layers
        beta : float
            Beta limits the upper bound of search on maximizing layers
        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves
        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.
            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if game.active_player == self: #maximizing player
            return self.max_value(game, depth, alpha, beta)[1] 
        else:
            return self.min_value(game, depth, alpha, beta)[1] 

    def max_value(self, game, depth, alpha, beta): 
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0:
            return self.score(game, self), (-1, -1)

        best_score = float("-inf")
        legal_moves = game.get_legal_moves(self)
        if len(legal_moves)>0:
            best_move = legal_moves[randint(0,len(legal_moves)-1)]
        else:
            best_move= (-1,-1)
        for move in legal_moves:
            next_score, _ = self.min_value(game.forecast_move(move), depth-1, alpha, beta)
            if best_score < next_score:
                best_score = next_score
                best_move = move
            if best_score >= beta:
                return best_score, best_move
            alpha=max(alpha,best_score) #best (among explored) option along path to root for maximizer
        return best_score, best_move

    def min_value(self, game, depth, alpha, beta): 
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0:
            return self.score(game, self), (-1, -1)

        best_score = float("inf")
        legal_moves = game.get_legal_moves(game.get_opponent(self))
        if len(legal_moves)>0:
            best_move = legal_moves[randint(0,len(legal_moves)-1)]
        else:
            best_move= (-1,-1)
        for move in legal_moves:
            next_score, _ = self.max_value(game.forecast_move(move), depth-1, alpha, beta)
            if best_score > next_score:
                best_score = next_score
                best_move = move
            if best_score <= alpha:
                return best_score, best_move
            beta = min(beta, best_score) #best (among explored) option along path to root for minimizer
        return best_score, best_move
