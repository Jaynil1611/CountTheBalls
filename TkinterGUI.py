# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 08:18:43 2019

@author: Jaynil Gaglani
"""

from tkinter import Tk,Label,Button,messagebox

def login_verify():
  answer = messagebox.askyesno(title="your response",message = "Do you want to continue ?")
#  the above functon will return true for 'yes' response , else will return false
  if answer:
    messagebox.showinfo("PLEASE CONTINUE")
  else:
    messagebox.showinfo("Byee")
    
root = Tk()
root.title("MY FIRST FRAME")
root.geometry("600x400+300+200")       #dimensions and postion specification
w = Label(root,text="GOOD EVENING",bg="black",fg="white")
w.pack()                              #this places into centre of window
p = Label(root,text="HIIIIII")
p.place(x=30,y=60)                    #this places into custom position
m = Label(root,text="GOOD MORNING",bg="yellow",fg="red")
m.pack()

b = Button(root,text="LOGIN",bg="#494454",width=15,height=1,font=("OpenSans",13,"bold"),fg="white",command=login_verify)  #last arg is function call 
#           no parenthesis needed while calling a function
b.place(x=250,y=150,anchor='center')     #anchor is used for relative position to centre.


root.mainloop()