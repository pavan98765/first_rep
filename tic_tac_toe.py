from tkinter import *
from tkinter import messagebox

Player1 = 'X'
stop_game = False

def clicked (r):
    #player
    global Player1
    if Player1 == "X" and states [r] == 0 and stop_game == False:
        b [r].configure (text = "X")
        states [r] = 'X'
        Player1='O'
    if Player1 == 'O' and states [r] == 0 and stop_game == False:
        b [r].configure (text = "O")
        states [r] = 'O'
        Player1='X'
    check_for_winner ()

def check_for_winner ():
    global stop_game
    for i in range (0,3):
        if states [i] == states [i+3] == states [i+6] != 0:
            b [i].configure (bg = 'gray')
            b [i+3].configure (bg = 'gray')
            b [i+6].configure (bg = 'gray')
            stop_game = True
    for i in range (0,9,3):
        if states [i] == states [i+1] == states [i+2] != 0:
            b [i].configure (bg = 'gray')
            b [i+1].configure (bg = 'gray')
            b [i+2].configure (bg = 'gray')
            stop_game = True
    if states [0] == states [4] == states [8] != 0:
        b [0].configure (bg = 'gray')
        b [4].configure (bg = 'gray')
        b [8].configure (bg = 'gray')
        stop_game = True
    if states [2] == states [4] == states [6] != 0:
        b [2].configure (bg = 'gray')
        b [4].configure (bg = 'gray')
        b [6].configure (bg = 'gray')
        stop_game = True
    if stop_game:
        messagebox.showinfo ("Game Over", "Click to play again")
        for i in range (0,9):
            b [i].configure (text = "", bg = 'white')
            states [i] = 0
        stop_game = False

root = Tk ()
root.title ("Tic Tac Toe")

states = [0,0,0,0,0,0,0,0,0]

b = []
for i in range (0,9):
    b.append (Button (root, text = "", font = ('Arial 20 bold'), height = 3, width = 6, command = lambda r=i: clicked (r)))
    b [i].grid (row = int (i/3), column = i%3)

root.mainloop ()