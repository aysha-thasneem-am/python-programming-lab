lst = []
n = int(input("Enter number of elements : "))
print("Enter", str(n), " integers: ")
for i in range(0, n):
    ele = int(input())
    lst.append(ele*ele)     
print(lst)
