def GreatestNum(n1,n2,n3):
    if n1>n2:
        f1=n1
    else:
        f1=n2
    if f1>n3:
        return f1
    else:
        return n3

g=GreatestNum(21,24,22)
print(f"The greatest of 3 numbers is {g}")