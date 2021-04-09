##################################################################
# FILE : ex12.py
# WRITER : amitchen93, eliyahu
# EXERCISE : intro2cs ex12 2019
# DESCRIPTION: program that manages the logical game  for the
# game 4 in a row
##################################################################

import numpy

import tkinter as tk

import math

from .ai import*





class Game:
    """class of game objecy, which we play on"""

    ROWS = 6

    COLOUMNS = 7



    PLAYER_1 = 1

    PLAYER_2 = 2

    COMPUTER = 3



    def __init__(self):


        self.player_1 = 1

        self.player_2 = 2

        self.board = self.create_board()

        self.turn = 0

        self.game = False

        self.counter = 0

        self.legal_move = 1

        self.win_index = []


    def create_board(self):
        """create a board of game"""

        board = numpy.zeros((self.ROWS, self.COLOUMNS))


        return board



    def make_move(self, column):
        """method which gets the column where you want to place
        a disk. if column is full, out of bounds, or the game
        is finished - we get an Exception
        we decided to keep the numbers as numbers and not as
        constant because we because we have
        noticed that the constants create more confusion in this
        case after a conversation with lab support"""
    
        try:
        
                if 6 < column or column < 0 or self.is_full(column):
                    
                    raise Exception("Illegal move")
        
        
                else:
                
                    if self.game is False:
        
        
                        player = self.get_current_player()
        
                        row = self.check_free_row(column)
        
                        self.counter += 1
        
        
        
                        if player == 1 and self.legal_move == 1:
                
                            self.insert_color(row, column, player)
    
                            result = self.get_winner()
                
                            self.turn += 1
                                
                            return result
        
        
    
                        elif player == 2 and self.legal_move == 1:
        
    
                            row = self.check_free_row(column)
        
                            self.insert_color(row, column, player)
        
                            result = self.get_winner()
        
                            self.turn += 1
        
                            return result
            
                        else:
                                    
                            return -1
        

        except Exception as e:
        
            return -1
    
    

    def is_full(self, column):   
        """method which returns True if the cell in coloum is
        full or False if the cell is empty.
        we decided to keep the numbers as numbers and not as
        constant because we because we have
        noticed that the constants create more confusion in this
        case after a conversation with lab support"""


        board = self.board

        if self.board[(self.ROWS) - 1][column] == 1 or\
                self.board[(self.ROWS) - 1][column] == 2:

            return True


        else:

            return False

    

    def check_free_row(self, column):  
        """method which checks where we can put a disk
        in coloum. returns i which present the cell in coloum"""


        for i in range(self.ROWS):

            if self.board[i][column] == 0:

                return i



    def insert_color(self, row, column, color):  
        """method which change a specific cell's value
        in the board (list of lists)"""
    

        self.board[row][column] = color



    def get_winner(self):
        """method which returns the status (1 for win of
        1, 2 for win of 2, 0 for full board and a tie)
        we decided to keep the numbers as numbers and not as
        constant because we because we have
        noticed that the constants create more confusion in this
        case after a conversation with lab support"""


        player = self.get_current_player()


        for i in range(self.ROWS):

            for j in range(self.COLOUMNS - 3):

                if self.board[i][j] == player and\
                        self.board[i][j + 1] == player and\
                        self.board[i][j + 2] == player and\
                        self.board[i][j + 3] == player:

                    self.legal_move = 0
                    
                    self.game = True

                    for k in range(4):
                        self.win_index.append((i, j+k))
                    
                    
                    return self.get_current_player()


        for i in range(self.ROWS - 3):

            for j in range(self.COLOUMNS):

                if self.board[i][j] == player and\
                        self.board[i + 1][j] == player and\
                        self.board[i + 2][j] == player and \
                        self.board[i + 3][j] == player:

                    self.legal_move = 0
                    
                    self.game = True

                    for k in range(4):
                        self.win_index.append((i+k, j))


                    return self.get_current_player()

        for i in range(self.ROWS - 3):

            for j in range(self.COLOUMNS - 3):

                if self.board[i][j] == player and\
                        self.board[i + 1][j + 1] == player and\
                        self.board[i + 2][j + 2] == player and\
                        self.board[i + 3][j + 3] == player:

                   
                    self.legal_move = 0
                    
                    self.game = True

                    for k in range(4):
                        self.win_index.append((i+k, j+k))


                    return self.get_current_player()


        for i in range(3, self.ROWS):

            for j in range(self.COLOUMNS - 3):


                if self.board[i][j] == player and\
                        self.board[i - 1][j + 1] == player and\
                        self.board[i - 2][j + 2] == player and\
                        self.board[i - 3][j + 3] == player:

                   
                    self.legal_move = 0
                    
                    self.game = True

                    for k in range(4):
                        self.win_index.append((i-k, j+k))


                    return self.get_current_player()

        if self.counter == (self.ROWS * self.COLOUMNS):

            self.legal_move = 0
            
            self.game = True

            return 0  


    def get_player_at(self, row, col):
        """method which returns a disk of which player
        (1 or 2 or None if if empty) for AI
        we decided to keep the numbers as numbers and not as
        constant because we because we have
        noticed that the constants create more confusion in this
        case after a conversation with lab support"""


        try:

            if row not in range(6) or col not in range(7):



                raise Exception("Illegal location")



            else:


               if self.board[row][col] == 1:

                   return 1



               elif self.board[row][col] == 2:

                   return 2



               elif self.board[row][col] == 0:

                   return None



        except Exception as e:

               return -1



    def get_current_player(self):
        """method which returns the current player
        should play (if turn id odd or even)
        we decided to keep the numbers as numbers and not as
        constant because we because we have
        noticed that the constants create more confusion in this
        case after a conversation with lab support"""



        if self.turn % 2 == 0:

           
            return 1



        else:




            return 2


