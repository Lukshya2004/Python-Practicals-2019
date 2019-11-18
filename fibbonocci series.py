i=int(input("enter the limit"))
x=0
y=1
z=1
print("fibonocci series is")
print(x,y,end=" ")
for i in range(2,i):
    print(z,end=" ")
    x=y
    y=z
    z=x+y
