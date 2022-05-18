# Use open function to read the contents of a file

# f=open("sample.txt",'r')  #if you don't mention the mode(here'r'),it takes r as default
f=open("sample.txt") 
data=f.read()
print(data)
f.close()


f=open("sample.txt") 
data=f.read(2)  #specify nuber of characters(not words) we want to read
print(data)
f.close()

