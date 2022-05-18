num=int(input("Enter the number: "))
prime=False
if num<0:
    print("Enter a positive number")

if num==1 or num==0:
    print("the number is not a prime number")
    

if num>1:
    for i in range(2,num):
        if num%i==0 :
            prime=True
            break

    if prime:
        print("the number is not a prime number")
    else:
        print("the number is a prime number")


