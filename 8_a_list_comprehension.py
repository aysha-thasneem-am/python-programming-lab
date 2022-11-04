list1=[]
n = int(input("Enter number of elements : "))
print("Enter", str(n), " integers: ")
for i in range(0, n):
    ele = int(input())
    list1.append(ele)
new_list=[x for x in list1 if x>0]
print(new_list)
