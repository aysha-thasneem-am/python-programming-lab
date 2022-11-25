def length_of_longest(words):
	return max([len(word) for word in words])

a=input("Enter A List of Words : ").split()
print(length_of_longest(a))
