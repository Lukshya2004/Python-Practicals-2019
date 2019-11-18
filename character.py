C=input("enter the character")
N=int(input("Enter no of rows:"))
for I in range(1,N+1):
    for K in range(1,I+1):
        print(C,"\t",end="")
    print("\n")
