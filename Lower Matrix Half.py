list = []
m= int(input())
n = int(input())
for i  in range(m):
    r1 = []
    for j in range(n):
        r1.append(int(input()))
    list.append(r1)
for i in range(m):
    for j in range(n):
        print(list[i][j], "\t",end ="")
    print()
for i in range(m):
    for j in range(i+ 1):
        print(list[i][j], "\t",end ="")
    print()
    
