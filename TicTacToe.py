from tkinter import *
import random

def next_turn():
    pass


def check_winner():
    pass


def empty_spaces():
    pass


def new_game():
    pass


window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]
player = random.choice(players)
button = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas', 40))
label.pack()

reset_button = Button(text="restart", font=)
