l=int(input("Enter the length of rectangle: "))
b=int(input("Enter the breadth of rectangle: "))
def area():
    area=l*b
    print("Area of rectangle with length ",l," and breadth ",b," is: ",area)
def perimeter():
    perimeter=2*(l+b)
    print("Perimeter of rectangle with length ",l," and breadth ",b," is: ",perimeter)
area()
perimeter()
