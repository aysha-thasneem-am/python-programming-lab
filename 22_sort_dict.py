dict={}
n=int(input("Enter No of Elements in Dictionary : "))
for i in range(n):
	key=input("\nEnter the Key : ")
	value=input("Enter the Value : ")
	dict[key]=value

a_s_dict=sorted(dict.items(),reverse=0)
d_s_dict=sorted(dict.items(),reverse=1)


print("\nAscending Order : ",a_s_dict)
print("\nDescending Order : ",d_s_dict)
