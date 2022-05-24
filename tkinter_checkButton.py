from tkinter import *
window=Tk()
window.title("Programming Course")
l1=Label(window,text="Choose Your Course")
l1.grid(row=0,column=0) 
cb1=Checkbutton(window,text="Python")
cb1.grid(row=0,column=1)
window.mainloop()