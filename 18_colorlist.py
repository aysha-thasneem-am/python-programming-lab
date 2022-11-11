a=input("Enter Colour List 1 : ")
b=input("Enter Colour List 2 : ")
a=a.split(" ")
b=b.split(" ")
c=[x for x in a if x not in b]
print("List 1 - ",a)
print("List 2 - ",b)
print("Colours in List 1 Not in List 2 - ",c)
