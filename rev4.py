import math
c = 50
h = 30
d = []
n = int(input())
for i in range(n):
    d.append(int(input()))
print(d)
for i in range(n):
    print(math.sqrt((2*c*d[i])//h))
