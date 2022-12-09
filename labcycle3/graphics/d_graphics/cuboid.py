def area_cuboid():
    l=int(input("Enter the length of cuboid: "))
    b=int(input("Enter the breadth of cuboid: "))
    h=int(input("Enter the height of cuboid: "))
    area=2*(l*b + b*h + h*l)
    print("Total Surface Area of cuboid with length ",l,", breadth ",b,", and height ",h," is: ",area)
def vol_cuboid():
    l=int(input("Enter the length of cuboid: "))
    b=int(input("Enter the breadth of cuboid: "))
    h=int(input("Enter the height of cuboid: "))
    volume=l*b*h
    print("Volume of cuboid with length ",l,", breadth ",b,", and height ",h," is: ",volume)
