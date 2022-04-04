import tkinter as tk
from tkinter import *
import random

#Открытие игрового окна (2)
def startGame():
    print("Starting game")
    firstW.destroy()
    secondW = tk.Tk()
    charName = tk.Label(text = name, fg = 'Black')
    charName.pack()
    secondW.mainloop()    

firstW = tk.Tk()

hello = tk.Label(
    text="Hello, my name is...",
    fg="#003844",
    bg="#FFB100"
)

inputName = tk.Entry()

name = inputName.get()

playBt = tk.Button(
    text=("Let's start"),
    bg="#F194B4",
    fg="#003844",
    command=startGame
)



hello.pack()
inputName.pack()
playBt.pack()
firstW.mainloop()

