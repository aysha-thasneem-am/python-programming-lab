def ing_fun(a):
	if (a[-1]=='g') and (a[-2]=='n') and (a[-3]=='i'):
		b=a+'ly'
	else:
		b=a+'ing'
	print(b)
a=input("Enter A String : ")
ing_fun(a)
