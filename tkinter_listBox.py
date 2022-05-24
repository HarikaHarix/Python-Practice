# insert and eliminate items from list box

from tkinter import *
window=Tk()
window.title("Learning Tkinter")
window.minsize(width=500,height=300) 
window.maxsize(width=1000,height=600)
lb=Listbox(window,width=20)
lb.pack()
l1=["Harry","Hermione","Ron","Hadrid"]
for i in l1:
    lb.insert(END,i)
def remove():
    lb.delete(ANCHOR)
b1=Button(window,text="remove",bg="pink",fg="black",command=remove).pack()
window.mainloop()
