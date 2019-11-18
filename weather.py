list = []
m = int(input())
n = int(input())
for i in range(m):
    r1 = []
    for j in range(n):
        r1.append(input())
    list.append(r1)
for i in range(m):
    for j in range(n):
        print(list[i][j],"\t", end = "")
    print()
a1 = 0
a2 = 0
a3 = 0
for k in list:
    if list[i][j] == "Rainy":
        a1 += 1
    elif list[i][j] == "Sunny":
        a2 += 1
    else:
        a3 += 1
print(a1)
print(a2)
print(a3)
