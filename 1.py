from tkinter import *
import calendar

text=calendar.calendar(2021)

root=Tk()
root.geometry("550x650")
root.title("CALENDAR")
label1=Label(root,text="CALENDAR 2021", bg='dark gray', font=("times",22,'bold'))
label1.grid(row=1,column=2)
root.config(background="white")
l1=Label(root,text=text,font="Consolas 10 bold")
l1.grid(row=2,column=2,padx=20)
root.mainloop()
