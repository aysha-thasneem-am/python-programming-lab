def pattern(n):
	num = 1
	for i in range(0, n):
		for j in range(0, i+1):
			print(num, end=" ")
			num = num + 1
		print()
n = int(input("Enter the no. of rows: "))
pattern(n)
