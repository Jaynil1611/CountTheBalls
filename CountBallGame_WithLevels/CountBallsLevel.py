# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 20:52:39 2019

@author: Jaynil Gaglani
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:39:48 2019

@author: Jaynil Gaglani
"""

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

def startclick(level = 0):
    global i
    global redCount
    global greenCount
    global canvas
    
    for i in range(1,3*(level+5)):
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

def getCount():
    global canvas 
    global redCount 
    global greenCount 
    if redCount==int(t1.get()) and greenCount==int(t2.get()):
      messagebox.showinfo("RESULT ","YOU HAVE CORRECTLY GUESSED THE ANSWER")
    else:
      messagebox.showerror("RESULT ","YOU ARE INCORRECT")
      
def timerfun():
        messagebox.showinfo(title = "ANSEWER  ",message = "Number of Red Balls = " + str(redCount) + " Number of Green Balls = " + str(greenCount))
        canvas.delete("all")
        t1.delete(0,'end')
        t2.delete(0,'end')
      
def startgame(level = 0):
    global canvas                  #this global keyword is used to point to global canvas variable.
    global i
    if(level == 0):
      x  = startclick(0)
    else:
      x = startclick(level)
    if x==1:
        time.sleep(0)             #the computer waits for user
        root.after(10000-(2*level*1000),timerfun)


root = Tk()
root.title("COUNT THE COLORS")
root.geometry("900x650+300+40")

canvas = Canvas(width = 500,height = 500,bg = "#20b2aa")       #same as JPanel in JFrame
canvas.place(x = 20 , y = 20)

w = Label(root,text = "Can you count the number of RED and GREEN coloured balls ?",fg="white",bg="black")
w.place(x = 20,y = 500)

y = Label(root,text = "You have 10 seconds to answer ...Press START button to Play !!! ",fg="white",bg="#78d89c")
y.place(x = 20,y = 550)

l1 = Label(root,text = "Input No. of Red Balls  ",fg="white",bg="black")
l1.place(x = 650, y = 200)
t1 = Entry(root)
t1.place(x = 650, y = 230)


l2 = Label(root,text = "Input No. of Green Balls ",fg="white",bg="black")
l2.place(x = 650, y = 300)
t2 = Entry(root)
t2.place(x = 650, y = 330)

level1 = Button(text = "LEVEL1", bg = "#b83737", width = 20, height =1,font= ("TimeNewRoman",13,"bold"), fg = "red", command = lambda:startgame(1))
level1.place(x =650, y = 30)


level2 = Button(text = "LEVEL2", bg = "#b83737", width = 20, height =1,font= ("TimeNewRoman",13,"bold"), fg = "red", command = lambda:startgame(2))
level2.place(x =650, y = 70)


level3 = Button(text = "LEVEL3", bg = "#b83737", width = 20, height =1,font= ("TimeNewRoman",13,"bold"), fg = "red", command = lambda:startgame(3))
level3.place(x =650, y = 110)                
              
b = Button(root, text = "SUBMIT", bg = "#ffe4e9", width = 20, height = 1, font=("TimeNewRoman",13,"bold"),fg="red",command = getCount)
b.place(x = 650,y = 400)

b = Button(root, text = "START", bg = "#ffe4e9", width = 20, height = 1, font=("TimeNewRoman",13,"bold"),fg="red",command = startgame)
b.place(x = 20,y = 600)






#Make timer or new frame for input
#Assign variables for levels in which  
#Level 1 , 2  , 3
#Next sunday 11:30-2:30

















root.mainloop()