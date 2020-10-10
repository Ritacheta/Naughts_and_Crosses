# Naughts_and_Crosses

## Description
I wanted to modify the Tic-Tac-Toe game by using Artificial Intelligence(ai) in the server side. It's has made the server automatic. So we need not to hesitate about inputting in the server side. For making the server smart I have used **MinimaxAlgorith** to predict the next step from the server. 

## Minimax Algorithm
Minimax is a kind of backtracking algorithm that is used in decision making and game theory to find the optimal move for a player, assuming that your opponent also plays optimally. It is widely used in two player turn-based games such as Tic-Tac-Toe, Backgammon, Mancala, Chess, etc.

In Minimax the two players are called maximizer and minimizer. The maximizer tries to get the highest score possible while the minimizer tries to do the opposite and get the lowest score possible.

Every board state has a value associated with it. In a given state if the maximizer has upper hand then, the score of the board will tend to be some positive value. If the minimizer has the upper hand in that board state then it will tend to be some negative value. The values of the board are calculated by some heuristics which are unique for every type of game.

## My Approach
I have implement minimax function in the server side that evaluates the probablity of winning by tracking the position of others input. Simply it checks in which direction the probablity of winning is most and the instruct the an other function to return the position.

