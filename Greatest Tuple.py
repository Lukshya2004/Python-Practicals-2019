t = ()
m = int(input())
n = int(input())
for i in range(m):
    t1 =()
    for j in range(n):
        t1 += (int(input()),)
    t += (t1,)
for i in range(m):
    for j in range(n):
        print(t[i][j],"\t", end = "")
    print()

for i in range(m):
    greatest = 0
    for j in range(n):
        if t[i][j] > greatest:
            greatest = t[i][j]
            break
        else:
            print(greatest)
    print(greatest)
print(t)
