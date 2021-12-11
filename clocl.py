


import sys
from tkinter import *
import time


def times():
	current_time=time.strftime("%A:%d:%B:%Y")
	clock.config(text=current_time)
	clock.after(200,times)

root=Tk()
root.geometry("1011x400")
clock=Label(root,font=("times",50,"bold"),bg="white")
clock.grid(row=2,column=2,pady=25,padx=100)
times()

digi=Label(root,text="Digital Clock", font=("times", 24, "bold") )
digi.grid(row=0,column=2)

nota=Label(root,text=        		"    DAY :DATE : MONTH : YEAR " , font=("times",50 ))
nota.grid(row=3,column=2)



def times():
	current_time=time.strftime("%I:%M:%S")
	clock.config(text=current_time)
	clock.after(200,times)

clock=Label(root,font=("times",50,"bold"),bg="white")
clock.grid(row=5,column=2,pady=25,padx=100)


nota=Label(root,text=      "Hours   : Minutes  : Seconds   " , font=("times",15 , "bold"))
nota.grid(row=4,column=2)







root.mainloop()