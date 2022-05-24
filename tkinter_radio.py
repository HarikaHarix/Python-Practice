from tkinter import *
window=Tk()
window.title("Learning Tkinter")
window.minsize(width=500,height=300)  #minimum size of our window
window.maxsize(width=1000,height=600)
v=IntVar()
def clicked():
    print(v.get())
rd1=Radiobutton(window, text="yes",value=1,variable=v) #values are return so that only one option is selected at once
rd1.grid(row=10,column=10)
rd2=Radiobutton(window,text="no",value=0,variable=v)
rd2.grid(row=11,column=10)
b1=Button(window,text="Enter",command=clicked)   #you'll get 1 for yes and 0 for no in output
b1.grid(row=12,column=10)
window.mainloop()
