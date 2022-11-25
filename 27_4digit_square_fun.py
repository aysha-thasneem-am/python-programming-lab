a=[]
def perfsq_fun(n):
	for i in range(1000,n+1):
		if (i**(.5) == int(i**(.5))):
			a.append(i)

n=int(input("Enter A 4 Digit Limit : "))
perfsq_fun(n)
print(a)
