value=int(input("Enter the limit: "))
a=[]
for i in range(value):
    num=int(input("enter integer: "))
    if(num>100):
        num="over"
    a.append(num)
print(a)
