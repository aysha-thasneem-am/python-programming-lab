a=input("Enter A String : ")
a=a.lower()
length=len(a)
x=a[0]
y=a[length-1]
z=a.replace(x,y,1)
r=z[:length-1]+x
print(r)
