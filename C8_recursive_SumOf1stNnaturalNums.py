

# Python program to find the sum of natural using recursive function

def recur_sum(n):
    if n==1 or n==0:
       return n
    elif n<0:
        print("Enter positive number")
    else:
       return n + recur_sum(n-1)

num = int(input("Enter the number:"))
print("The sum is",recur_sum(num))