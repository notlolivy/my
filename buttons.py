from ast import Continue
from cgitb import text
from tkinter import *
import random
import time


root = Tk()
root.configure(background='black')
root.geometry("350x275")



#timeleft

def countdown(count):
    # change text in label        
    label['text'] = count
    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
    else: 
        gameover()

countdown1 = Label(root, text= "Time left: ", font= 20, fg= 'white', bg='black')
countdown1.pack()
label = Label(root, font= 20, fg= 'red', bg='black')
label.pack()

# call countdown first time    
countdown(10)



#commands

global score
score = 0
#change color



colorlist = ['red', 'green', 'yellow', 'blue']
colorlist1 = ['green', 'blue', 'red', 'yellow']

actualcolor= random.choice(colorlist)
random.shuffle(colorlist)
textcolor= random.choice(colorlist)
def red():
    if colorlist[1] == 'red':
        global score
        score += 1
        textcolor.replace(random.choice(colorlist), str(colorlist[1]))
        score1.config(text= "Your Score: " + str(score))
        if countdown == '0':
            return
        else: 
            random.shuffle(colorlist)
            directions1.config(fg = str(colorlist[1]), text = str(colorlist[0]))       
    else:
        wrong2 = Label(root, text="bruh", font= 20, fg= 'white', bg='black')
        wrong2.pack(side=BOTTOM)
        gameover()
        

def yellow():
    if colorlist[1] == 'yellow':
        global score
        score += 1
        score1.config(text= "Your Score: " + str(score))
        if countdown == '0':
            red.config(text= "\n")
            return
        else: 
            random.shuffle(colorlist)
            directions1.config(fg = str(colorlist[1]), text = str(colorlist[0]))             
    else:
        wrong2 = Label(root, text="bruh", font= 20, fg= 'white', bg='black')
        wrong2.pack(side=BOTTOM)
        gameover()
        

def green():
    if colorlist[1] == 'green':
        global score
        score += 1
        score1.config(text= "Your Score: " + str(score))
        if countdown == '0':
            red.config(text= "\n")
            return
        else: 
            random.shuffle(colorlist)
            directions1.config(fg = str(colorlist[1]), text = str(colorlist[0]))        
    else:
        wrong3 = Label(root, text="bruh", font= 20, fg= 'white', bg= 'black')
        wrong3.pack(side=BOTTOM)
        gameover()
        

def blue():
    if colorlist[1] == 'blue':
        global score
        score += 1
        score1.config(text= "Your Score: " + str(score))
        if countdown == '0':
            red.config(text= "\n")
            return
        else: 
            random.shuffle(colorlist)
            directions1.config(fg = str(colorlist[1]), text = str(colorlist[0]))      
    else:
        wrong4 = Label(root, text="bruh", font= 20, fg= 'white', bg= 'black')
        wrong4.pack(side=BOTTOM)
        gameover()
        



def gameover():
    for widgets in root.winfo_children():
      widgets.destroy()
      pass

    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("350x275")
    newWindow.configure(background='black')
    texts= Label(newWindow, text= "Game Over" + "\n" + "Your score: " + str(score), font= (NORMAL, 20), fg= 'white', bg='black')
    texts.pack()

     
        


#scoreboard
score = 0
score1= Label(root, text = "Your score: " + str(score), font= 20, fg= 'white', bg='black')
score1.pack()

#colors

name = Label(root, text= "What is the text color?", font= 20, fg= 'white', bg='black')
name.pack()

directions1 = Label(root, text= random.choice(colorlist1), font= (NORMAL, 30), fg= colorlist[1], bg='black')
directions1.pack()

red = Button(root, text= "red", bg="gold2", command= red)
yellow  = Button(root, text= "yellow", bg="cyan4", command= yellow)
blue = Button(root, text= "blue", bg="Deeppink4", command= blue)
green = Button(root, text= "green", bg="orange red", command= green)

red.pack()
yellow.pack()
blue.pack()
green.pack()

#game




root.mainloop()
