dict1={}
n=int(input("Enter the no.of items in the dictionary:"))
for i in range(n):
    key=input("Enter key: ")
    value=input("Enter value: ")
    dict1[key]=value
print(dict1)

dict2={}
m=int(input("Enter the no.of items in the dictionary:"))
for i in range(m):
    key=input("Enter key: ")
    value=input("Enter value: ")
    dict2[key]=value
print(dict2)
#dict1.update(dict2)
#print(dict1)

dict3={**dict1,**dict2}
for x,y in dict3.items():
    if x in dict1 and x in dict2:
        dict3[x]=[y,dict1[x]]

print(dict3)
