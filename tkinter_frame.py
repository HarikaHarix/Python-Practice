from tkinter import *
window=Tk()
window.title("Tkinter")
window.minsize(width=400,height=500)
window.maxsize(width=800,height=1000)

f1=Frame().pack()
f2=Frame()
f2.pack(side=BOTTOM)
l1=Label(f1,text=("sky")).pack()
l2=Label(f2,text="Water").pack()
window.mainloop()