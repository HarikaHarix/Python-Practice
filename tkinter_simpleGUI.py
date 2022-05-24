from tkinter import *
window=Tk()
window.title("WorldefyMe")
window.minsize(height=400,width=700)
window.maxsize(height=800,width=1400)

v=StringVar()
def clicked():
    x=v.get()
    print(x)
    l2.config(text=x,bg="yellow",fg="red")

l1=Label(window,text="Employee Name",font=("Arial",14),fg="white",bg="blue")
l1.grid(row=0,column=0)
l2=Label(window,text="none",bg="yellow",fg="green",font=("FuturaBold",14))
l2.grid(row=0,column=3)
e1=Entry(window,width=10,bd=5,font=("CopperPlate",14),textvariable=v)
e1.grid(row=0,column=1)
b1=Button(window,text="Enter",bg="green",fg="yellow",font=("Futura",14),command=clicked)
b1.grid(row=0,column=2)
window.mainloop()