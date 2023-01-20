fn=open("mom.txt","r")
fn1=open("oddline.txt",'w')
cont=fn.readlines()

for i in range(0,len(cont)):
    if(i % 2==0):
        fn1.write(cont[i]+"\n")
    else:
        pass
fn1.close()
fn1=open('oddline.txt','r')
cont1=fn1.read()
print(cont1)
fn.close()
fn1.close()
