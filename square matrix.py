lst = []
rows = int(input())
for i in range(rows):
    r1 = []
    for j in range(rows):
        r1.append(int(input()))
    lst.append(r1)
for i in range(rows):
    for j in range(rows):
        print(lst[i][j],"\t", end = "")
    print()

sum = 0
for i in range(rows):
    sum += lst[i][i]
s1 = 0
for i in range(rows - 1, -1 , -1):
    s1 += lst[i][i]
print((s1 + sum))
