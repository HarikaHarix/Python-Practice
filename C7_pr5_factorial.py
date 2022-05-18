# n!=1*2*3*4*...*(n-1)*n

num=int(input("Enter the number: "))
factorial=1
if num<0:
    print("Enter a positive number")
# if num==1 or num==0:
#     print(f"the factorial of {num} is 1")   #without this the code will work for fact of 0 as we gave it initially
for i in range(1,num+1):
    factorial=factorial*i
print(f"the factorial of {num} is {factorial}")


# factorial of given number
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
 
# Driver Code
num = 5
print("Factorial of",num,"is",factorial(num))

 