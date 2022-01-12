"""Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row,
 a column, or a diagonal with either three x's or three o's drawn in the 
 spaces of a grid of nine squares."""

"""Tic-Tac-Toe is played according to the following rules.

The game is played on a grid that is three squares by three squares.
Player one uses x's. Player two uses o's.
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
If all nine squares are full and neither player has three in a row, the game ends in a draw.
"""

'''
Tic-Tac-Toe: Game
Author: Bro. Eugene Kartey
'''
import random

def main():
    

    while game_in_progress:
        create_board(board)
        player_input(board)
        checkwin()
        chktie(board)
        switch_player()
        computer(board)
        checkwin()
        chktie(board)

    print("Good game. Thanks for playing!") 
        



board=["-","-","-",
        "-","-","-",
        "-","-","-"]
    
current_player = "X"
winner = None
game_in_progress = True

#creating the tictactoe board

def create_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    

#Player input
   
def player_input(board):
    
    user_input = int(input('Please a number 1-9: '))
    
    if user_input >= 1 and user_input <= 9 and board[user_input - 1] == "-":
        board[user_input-1] = current_player
        
    else:
        print('The space has already been filled. Try again!')
    

#check win in horizontal, vertical and diagonal of the board

def chkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1]  != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3]  != "-":
        winner = board[3]
        return True
    elif  board[6] == board[7] == board[8] and board[6]  != "-":
        winner = board[6]
        return True

def chkvertrow(board):
    global winner 
    if board[0] == board[3] == board[6] and board[0]  != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1]  != "-":
        winner = board[1]
        return True
    elif  board[2] == board[5] == board[8] and board[6]  != "-":
        winner = board[2]
        return True
    

def chkdiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0]  != "-":
        winner = board[0]
        return True
    elif board[6] == board[4] == board[2] and board[6]  != "-":
        winner = board[6]
        return True
   
# checking tie

def chktie(board):
    global game_in_progress
    if "-" not in board:
        create_board(board)
        print('It is a tie!')
        game_in_progress = False

#checking win

def checkwin():
    global game_in_progress
    if chkhorizontal(board) or chkvertrow(board) or chkdiag(board):
        print(f'The winner is {winner}')
        game_in_progress = False

# switching players

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


# Player2 is computer
def computer(board):
    while current_player == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()



if __name__ == "__main__":
    main()