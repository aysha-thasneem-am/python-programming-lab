a=input("Enter Numbers : ")
a=a.split(" ")
b=[]
for i in a:
	b.append(int(i))
c=[x for x in b if x%2!=0]
print(b)
print("After Remving Even Numbers : ")
print(c)
