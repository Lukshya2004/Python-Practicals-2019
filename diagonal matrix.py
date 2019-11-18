m = []
rows = int(input())
for i in range(rows):
    r1 = []
    for j in range(rows):
        r1.append(int(input()))
    m.append(r1)
for i in range(rows):
    for j in range(rows):
        print(m[i][j], "\t", end = "" )
    print()
sum = 0
for i in range(rows):
    sum += m[i][i]
print(sum)
