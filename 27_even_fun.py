import math
        
n=int(input("Enter the lower limit: "))
m=int(input("Enter the upper limit: "))

def is_even():
    a=[]
    b=[]
    for i in range(n,m):
        k=i
        f=0
        while i>0:
            d=i%10
            if d%2!=0:
                f=1
                break
            else:
                i=i//10
        if f==0:
            a.append(k)
    for j in a:
        s=(int(math.sqrt(j)))*(int(math.sqrt(j)))
        if s==j:
            b.append(j)
    print(b)

if ((n>999 and n<10000) and (m>n and m<10000)):
    is_even()
else:
    print("Enter a valid 4-digit limit!")

