# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 09:06:19 2019

@author: Jaynil Gaglani
"""

from tkinter import *
import random
import time
from tkinter import ttk
from tkinter import messagebox

colours=["blue","red","yellow","green","red","pink","red","black","green","cyan"]
global i
i = 0
global redCount
redCount = 0
global greenCount
greenCount = 0
global canvas

def startclick():
    global i
    global redCount
    global greenCount
    global canvas
    
    for i in range(1,10):
        m = random.randint(0,10)
        if m==1 or m==4 or m==6:
          redCount+=1
        if m==3 or m==8:
          greenCount+=1
        try:
          a = random.randint(50,250)
          b = random.randint(50,300)
          canvas.create_oval(a, b, a+50, b+50, outline="white", fill = colours[m],width = 2)
          canvas.update()
        except:
          print("Exception Occured...")
    return 1

def startgame():
    global canvas                  #this global keyword is used to point to global canvas variable.
    x  = startclick()
    if x==1:
        time.sleep(5)             #the computer waits for user 
        messagebox.showinfo(title = "ANSEWER  ",message = "Number of Red Balls = " + str(redCount) + " Number of Green Balls = " + str(greenCount))
        canvas.delete("all")
    
    
root = Tk()
root.title("COUNT THE COLORS")
root.geometry("900x650+300+40")

canvas = Canvas(width = 500,height = 500,bg = "#20b2aa")       #same as JPanel in JFrame
canvas.place(x = 20 , y = 20)

w = Label(root,text = "Can you count the number of RED and GREEN coloured balls ?",fg="white",bg="black")
w.place(x = 20,y = 500)

y = Label(root,text = "You have 10 seconds to answer ...Press START button to Play !!! ",fg="white",bg="#78d89c")
y.place(x = 20,y = 550)

b = Button(root, text = "START", bg = "#ffe4e9", width = 20, height = 1, font=("TimeNewRoman",13,"bold"),fg="red",command = startgame)
b.place(x = 20,y = 600)
























root.mainloop()