a=[]
b=[]
n=int(input("size of a:"))
m=int(input("size of b:"))
for i in range(1,n+1):
    c=int(input("Enter the elements of a:"))
    a.append(c)
for i in range(1,m+1):
    d=int(input("Enter the elements of b:"))
    b.append(d)
print("List 1:",a,"\nList 2:",b)
print("\n1.check whether the list are of same length \n2.check whether the two list are of same value \n3.check whether any value occur in both the list\n")
while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        if n==m:
            print("List are of same length.")
        else:
            print("List are of different length.")
    elif ch==2:
        a.sort()
        b.sort()
        if a==b:
            print("List are identical.")
        else:
            print("List are not identical.")
    elif ch==3:
        c=[]
        for x in a:
            for y in b:
                if (x==y):
                    c.append(x)
        if (len(c)!=0):
            print("The value",c,"occur in both list. \n")
        else:
            print("No similar value occur in both list.")
    else:
        print('Invalid entry.')
    y=input("Do you want to continue?(yes/no):")
    if y.lower()=="yes":
        continue
    else:
        break
