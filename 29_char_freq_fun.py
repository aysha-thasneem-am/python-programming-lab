def char_count_fun(a):
	b=[]
	for i in a:
		if i not in b:
			b.append(i)
#print(b)

	for i in range(0,len(b)):
		print(b[i]," repeats ",a.count(b[i])," time(s)")

a=input("Enter A String : ")
char_count_fun(a)
