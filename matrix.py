M = []
r = int(input())
c = int(input())
for i in range(r):
    r1 = []
    for j in range(c):
        r1.append(int(input()))
    M.append(r1)
for i in range(r):
    for j in range(c):
        print(M[i][j],"\t",end = " ")
    print()
        
