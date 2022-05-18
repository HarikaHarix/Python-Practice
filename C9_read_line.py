
from tkinter import W


f=open("sample.txt",'r') 
data=f.readline() #reads only first line
print(data)
data=f.readline() #reads the next line
print(data)
f.close() 

#rt--> read in text mode. Even if you write r it'll take it as rt by default
#rb--> read in binary mode. do mention rb for sure

#r--open for reading
#w--open for writing
#a--open for appending
#+--open for updating

