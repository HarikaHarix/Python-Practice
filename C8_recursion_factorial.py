#USING FUNCTION

num=int(input("Enter the number: "))

def factorial_iter(n):
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    # print(f"the factorial of {num} is {factorial}")   #giving extra none in the output
    return factorial

print(f"The factorial of {num} is {factorial_iter(num)}")

# USING RECURSION

# n!=(n-1)!*n

num1=int(input("Enter the number: "))
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial_recursive(n-1)
print(f"The factorial of {num1} is {factorial_recursive(num1)}")


