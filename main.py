import tkinter as tk
from tkinter import *
import random


#Открытие игрового окна (2)
def startGame():
    
    life = 3
    def kill():
        pass
    

    print("Starting game")
    
    firstW.destroy()
    secondW = tk.Tk()
    


    charName = tk.Label(
        text = name.get(), 
        fg="#003844",
        bg="#FFB100"
        )

    health = tk.Label(
        text = life,
        fg="#003844",
        bg="#F194B4"
        )

    killBt = tk.Button(
        fg="#003844",
        bg="#F194B4",
        command=kill)


    charName.pack(side=LEFT)
    health.pack(side=LEFT)
    killBt.pack(side=LEFT)
    secondW.mainloop()


firstW = tk.Tk()

hello = tk.Label(
    text="Hello, my name is...",
    fg="#003844",
    bg="#FFB100"
)

name = StringVar()

inputName = tk.Entry(textvariable=name)

playBt = tk.Button(
    text=("Let's start"),
    bg="#F194B4",
    fg="#003844",
    command=startGame
)



hello.pack(side=LEFT)
inputName.pack(side=LEFT)
playBt.pack(side=LEFT)
firstW.mainloop()

