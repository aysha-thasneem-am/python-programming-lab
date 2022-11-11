b=[]
num=int(input("enter the size of the list:"))
for i in range(0,num):
    a=input("enter any words into list:")
    b.append(a)
print(b)
count=0
for elem in b:
    for j in elem:
        if(j=="a" or j=="A"):
            count=count+1
print("occurence of a:",count)
