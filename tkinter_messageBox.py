from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Learning Tkinter")
window.minsize(width=500,height=300)  #minimum size of our window
window.maxsize(width=1000,height=600)
v=StringVar()
def clicked():
    if v.get()=="":
        messagebox.showwarning("Caution","It's empty")
    else:
        messagebox.showinfo("successful",v.get())
e1=Entry(window,font=("calibri",14),width=20,textvariable=v)
e1.pack()
b1=Button(window,text="Enter", command=clicked)
b1.pack()
window.mainloop()
