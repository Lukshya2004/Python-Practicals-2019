value1 = input()
values = value1.split(",")
m = int(values[0])
n = int(values[1])
l= []
for i in range(m):
    b1 = []
    for j in range(n):
        b1.append(0)
    l.append(b1)
print(l)

for i in range(m):
    for j in range(n):
        l[i][j] = i*j

for i in range(m):
    for j in range(n):
        print(l[i][j],"\t", end ="")
    print()
