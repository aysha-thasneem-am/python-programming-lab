s = 0
def sum1(a):
    global s
    s+=a
    return s
li =list(map(int,input("Enter a numbers ").split()))
s=list(map(sum1,li))
print(s[-1])
