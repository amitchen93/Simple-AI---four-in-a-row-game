##################################################################
# FILE : ex12.py
# WRITER : amitchen93, eliyahu
# EXERCISE : intro2cs ex12 2019
# DESCRIPTION: program that manages Gui codes for the
# game 4 in a row
##################################################################



import tkinter as tk
from ex12.ai import*
from ex12.game import*
import time
from ctypes import*





class Gui_Open:
    """class of object that create a graphic version
     of the logical game that manage on game class for open screen"""


    def __init__(self,root):



        self.root = root
        
        
        self.size =  root.geometry("800x800") 
        
        self.bg = root.configure(background = "saddle brown")
        self.ttl = tk.Label(self.root, text = "Welcome to 4 in a Row!",
                            fg = "blue", font = "Verdana 32 bold italic",
                            width = 100).pack(padx = 60,pady = 40)
        
        
        
        self.button1 = tk.Button(self.root, text = "Player 1 vs Player 2",
                                 command = self.button_1, fg = "green",
                                 font = "Times" ).pack(padx = 100,pady = 50)
        self.button2 = tk.Button(self.root, text = "Player 1 vs Computer",
                                 command = self.button_2, fg = "green",
                                 font = "Times").pack(padx = 100,pady = 50)
        self.button3 = tk.Button(self.root, text = "Computer v Player 1",
                                 command = self.button_3, fg = "green",
                                 font = "Times").pack(padx = 100,pady = 50)
        self.button4 = tk.Button(self.root,
                                 text = "Computer v Computer",
                                 command = self.button_4,
                                 fg = "green",
                                 font = "Times").pack(padx = 100, pady = 50)
        self.exitbutton = tk.Button(self.root, text = "Exit",
                                    command = self.destroy_window,
                                    fg = "red",
                                    font = "Times").pack(padx = 100,pady = 50)
        

    def button_1(self):
        """take a part in the option of person vs
        person. uses callback 1"""

        
        root_2 = tk.Tk()
        g = Gui(root_2)
        g.draw_board()
        self.root.destroy()

        g.game_board.bind("<Button-1>", g.callback_1)




    def button_2(self):
        """take a part in the option of person vs
        computer. uses callback 2"""
       
        root_3 = tk.Tk()
        g = Gui(root_3)
        g.draw_board()
        self.root.destroy()
        
        g.game_board.bind("<Button-1>", g.callback_2)
        



    def button_3(self):
        """take a part in the option of computer vs
        person. uses callback 2 call to the computer"""
        
        root_4 = tk.Tk()
        g = Gui(root_4)
        g.draw_board()
        self.root.destroy()
        g.game.make_move(g.ai1.find_legal_move())

        root_4.update()
        time.sleep(1)

        g.draw_moves()
        g.root.update()
                           
        g.game_board.bind("<Button-1>", g.callback_2)
        



    def button_4(self):
        """call to the ai_v_ai (computer vs computer)"""
        root_5 = tk.Tk()
        g = Gui(root_5)
        g.draw_board()
        self.root.destroy()
        g.ai_v_ai()
        


    def destroy_window(self):
        """destroy a object of Gui"""
        
        self.root.destroy()
        
        

class Gui_final:
    """class of object appears in the end of the game"""

    def __init__(self, root):
    
        self.root = root
        self.size =  root.geometry("800x800") 
        
        self.bg = root.configure(background = "green")
        self.ttl = tk.Label(self.root, text = "Game Over!",
             fg = "blue", font = "Verdana 32 bold italic",
             width = 100).pack(padx = 60,pady = 40)
        self.rematch_button = tk.Button(
             self.root, text = "Rematch", command = self.rematch,
             fg = "blue", font = "Times" ).pack(padx = 100,pady = 50)
        self.quit_button = tk.Button(
             self.root, text = "Quit", command = self.quit_game,
             fg = "blue", font = "Times").pack(padx = 100,pady = 50)
     
    def rematch(self):
        """destroy the board and send us to the menu"""
    
        self.root.destroy()
        root_7 = tk.Tk()
        play_again = Gui_Open(root_7)
         
         
    def quit_game(self):
        """only destroy the board"""
        
        self.root.destroy()


class Gui:
    """class of object that create a graphic version
     of the logical game that manage on game class for open screen"""



    WIDTH = 700

    HEIGHT = 700

    SQUARE = 100



    def __init__(self, root):

        self.root = root

        self.destroyed = False

        self.game = Game()

        self.game_board = tk.Canvas(root, width = self.WIDTH,
                                    height = self.HEIGHT, bg = "blue")

        self.game_board.pack()

        self.ai1 = AI(self.game, 1)

        self.mouse = True 

        self.exitbutton = tk.Button(self.root, text = "Exit",
                                    command = self.destroy_game, fg = "red",
                                    font = "Times").pack(padx = 100,pady = 50)

        self.result = 0
        
        self.game_message =  self.game_board.create_text(
            350, 50,fill="snow",
            font="Times 20 italic bold",text="Playing...")



    def destroy_game(self):
        """destroy the object of Gui"""


       
        self.destroyed=True
        self.root.destroy()


    def draw_board(self):
        """draw a game board with colors and shapes with tkinter"""

        for r in range(Game.ROWS):

            for c in range(Game.COLOUMNS):

                self.game_board.create_rectangle((c*100,r*100 + 100),
                                                 ((c+1)*100,(r+1)*100 + 100),
                                                 fill = 'yellow')

                self.game_board.create_oval(
                    (c*100,r*100 + 100),((c+1)*100,
                                         (r+1)*100 + 100), fill = 'black')



    def draw_moves(self):
        """paint and put disks in the board"""
      

        for r in range(Game.ROWS):

            for c in range(Game.COLOUMNS):

                if self.destroyed:
                    return

                if self.game.board[r][c] == Game.PLAYER_1:

                    self.game_board.create_oval(
                        (c*100, 800 - (r*100 + 100)),
                        ((c+1)*100,
                         800 - ((r+1)*100 + 100)), fill = 'green')




                elif self.game.board[r][c] == Game.PLAYER_2:

                        self.game_board.create_oval(
                            (c*100, 800 - (r*100 + 100)),
                            ((c+1)*100,800 - ((r+1)*100 + 100)),
                            fill = 'red')



    
    def check_win(self):
        """check who is the winner, compare the winner index
        list to the index_list (which ceates in class Game), mark 4
        discs that wins the game and give a winning message
        to the relevant player"""
            
        if self.result == 1 or self.result == 2:
            
            for r in range(Game.ROWS):

                for c in range(Game.COLOUMNS):



                    if self.game.board[r][c] == Game.PLAYER_1 and\
                            self.result == 1 and\
                            (r,c) in self.game.win_index:


                       

                        self.game_board.create_oval(
                            (c*100, 800 - (r*100 + 100)),((c+1)*100,800 - (
                                    (r+1)*100 + 100)),
                            outline = 'blue', width = 6)
                        self.game_board.delete(self.game_message)

                        self.game_board.create_text(
                            350, 50,fill="snow",
                            font="Times 20 italic bold",
                            text="Player 1 wins!!!")

                      
                        self.root.update()

                        time.sleep(0.10)


                    elif self.game.board[r][c] == Game.PLAYER_2 and\
                            self.result == 2 and\
                            (r,c) in self.game.win_index:


                        self.game_board.create_oval((c*100,
                                                     800 - (r*100 + 100)),
                                                    ((c+1)*100,800 - (
                                                            (r+1)*100 + 100)),
                                                    outline = 'blue',
                                                    width = 6)
                        self.game_board.delete(self.game_message)


                        self.game_board.create_text(
                            350, 50, fill = "snow",
                            font="Times 20 italic bold",
                            text="Player 2 wins!!!")

                       

                        self.root.update()


                        time.sleep(0.10)



    def callback_1(self, event):
        """manage the game of person vs person"""

       



        column = event.x



        if not self.game.game:


            self.result = self.game.make_move(math.floor(column/100))
            self.draw_moves()

            self.root.update()
            self.check_win()


        if self.result == 1 or self.result == 2:
            self.check_win()

            self.destroy_game()

            root_6 = tk.Tk()
            final_screen = Gui_final(root_6)

            root_6.update()





    def callback_2(self, event):
        """manage the game of person vs computer (2 options)"""

        column = event.x

        if not self.game.game:

            self.result = self.game.make_move(math.floor(column/100))
            self.draw_moves()
            
            self.root.update()
          

        if (not self.game.game) and self.destroyed is False:
            self.game_board.unbind("<Button-1>")
            time.sleep(1)


            self.result = self.game.make_move(self.ai1.find_legal_move())
            self.draw_moves()




            self.root.update()
            if self.destroyed is False:
                self.game_board.bind("<Button-1>", self.callback_2)


        if self.result == 1 or self.result == 2:
            self.check_win()

            self.destroy_game()

            root_6 = tk.Tk()
            final_screen = Gui_final(root_6)

            root_6.update()


    def ai_v_ai(self):
        """manage the game of 2 ai players"""

        self.root.update()
        time.sleep(1)
        self.game_board.unbind("<Button-1>")


        while self.game.game is False and self.destroyed is False:



            self.result = self.game.make_move(self.ai1.find_legal_move())
            while self.result == -1:
                self.result = self.game.make_move(self.ai1.find_legal_move())

            self.draw_moves()

            self.root.update()
            time.sleep(1)

            if self.result == 1 or self.result == 2:
                self.check_win()
                self.root.destroy()
                root_6 = tk.Tk()
                final_screen = Gui_final(root_6)
                root_6.update()
    
        

    def make_move_gui(self):
        """connect between the act of player to the game board"""



        self.game.create_board()
        

if __name__ == '__main__':

    
    root_1 = tk.Tk()

    a = Gui_Open(root_1)

    root_1.mainloop()
















