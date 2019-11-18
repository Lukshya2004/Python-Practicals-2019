List = []
m = int(input())
n = int(input())
for i in range(m):
    r1 = []
    for j in range(n):
        r1.append(0)
    List.append(r1)
for i in range(m):
    for j in range(n):
        print(List[i][j], "\t", end = "")
    print()
l = ()
a = int(input())
for i in range(a):
    l.append(int(input()))
print(l)
for k in range(m):
    for u in range(n):
        x= int(input())
        List.append(x)
print(List)
