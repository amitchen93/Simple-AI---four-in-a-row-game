##################################################################
# FILE : ex12.py
# WRITER : amitchen93, eliyahu
# EXERCISE : intro2cs ex12 2019
# DESCRIPTION: program that manages ai play for the
# game 4 in a row
##################################################################

from random import randint



class AI:
    """class of artificial intelligence that manage the computer game"""



    def __init__(self, game, player):



        self.game = game

        self.player = player

        self.move = randint(0,6)



    def find_legal_move(self, timeout=None):
        """choose a random cell in the board and
        put there a disk in the right color
        we decided to keep the numbers as numbers and not as
        constant because we because we have
        noticed that the constants create more confusion in this
        case after a conversation with lab support"""

       
        self.move = randint(0,6)
       



        return self.move



    def get_last_found_move(self):
        return self.move







