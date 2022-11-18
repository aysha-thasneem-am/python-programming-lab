def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return (x * factorial(x-1))

num = int(input("Enter a number to check its factorial: "))
if num < 0:
    print("Factorial of ", num, " does not exist!")
else:
    print("The factorial of", num, "is", factorial(num))
