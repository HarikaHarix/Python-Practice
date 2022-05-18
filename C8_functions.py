def greet(name):
    print("good day!",name)
greet("harry")

def MySum(num1,num2):
    return(num1+num2)
s=MySum(5,55)
print(s)


def percentage(marks):
    # return ((marks[0]+marks[1]+marks[2]+marks[3]+marks[4])/500)*100
    return ((sum(marks)/500)*100)
marks1=[56,96,85,74,82]
percent=percentage(marks1)
print(percent)
