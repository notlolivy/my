from cgitb import text
from msilib.schema import Font
from tkinter import *
from tkinter.font import BOLD
import random
from turtle import bgcolor, color


root = Tk()
root.geometry("400x400")
root.title("Decisionmaker dot com please get me out")
list = []

entry = Entry(root, width= 50, textvariable=text)
entry.pack()

def submit():
    decision = Label(root, text=entry.get())
    decision.pack()
    list.append(entry.get())    
    entry.delete(0, END)



def goal():
    goal = Label(root, text="DO THIS: " + random.choice(list), font=(BOLD, 25), fg= "red")
    goal.pack(side= BOTTOM)


submit = Button(root,text="ADD",command=(submit))
submit.pack()

decide = Button(root,text="Choose for me", command = goal)
decide.pack()


choice = Label(root,text="Undecided on: ")
choice.pack()



root.mainloop()
