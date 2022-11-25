from math import sqrt
def even(n):
        string=str(n)
        for digit in string:
                if digit in '13579':
                        return False
                return True
def square(n):
        a=sqrt(n)
        b=int(sqrt(n))
        if (a==b):
                return True
        else:
                return False
lower=int(input("Enter 4-digit no. as The Lower limit: "))
upper=int(input("Enter 4-digit no. as The Upper limit: "))
if (len(str(lower))!=4 and len(str(upper))!=4):
        print("Invalid!")
else:
        for i in range(lower,upper):
                if even(i) and square(i):
                        print(i)
