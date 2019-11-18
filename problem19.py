 #problem19.exe
L=[ ]
G=0
position=-1
N=int(input("Enter number of elements you want to enter:"))
for J in range(N):
    num=int(input("Enter the number"))
    L.append(num)

for K in range(0,N):
    if K==0:
        G=L[K]
        position+=1
    else:
        if L[K]>G:
            G=L[K]
            position=K
        
print("The greatest number is",G)
print("position is",position)
