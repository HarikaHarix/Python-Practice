from tkinter import *
window=Tk()
i1=PhotoImage(file="C:/Users/ADMIN/Desktop/eagle.png")
l1=Label(window,image=i1) #after this geormetrical classes must be given like pack,grid or place
l1.pack()
window.mainloop()


# from PIL import ImageTk, Image  --> for jpg images
# img = ImageTk.PhotoImage(Image.open("xyz.jpg"))  
# l=Label(image=img)
# l.pack()