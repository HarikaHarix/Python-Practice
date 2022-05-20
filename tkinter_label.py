import tkinter 
window=tkinter.Tk()
#rename the window name
window.title("Tourism")
window.minsize(width=100,height=60)
#pack is used to show object in the window
label=tkinter.Label(window,text="worldefyme!",font=("Arial Bold",10))
label.grid(row=0,column=0)
window.geometry("500x200")

txt=tkinter.Entry(window,width=15)    #creating textbox using tkinter Entry class
txt.grid(column=1,row=0)
def clicked():
    res="welcome to "+txt.get()
    label.configure(text=res)
bt=tkinter.Button(window,text="Enter",command=clicked,bg="blue",fg="white")
bt.grid(column=2,row=0)
window.mainloop()


combo=tkinter.Combobox(window)
combo['values']=(1,2,3,4,5,"Text")
combo.current(3)
combo.grid(row=0,column=0)