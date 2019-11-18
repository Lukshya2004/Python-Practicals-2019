m = []
r = int(input())
for i in range(r):
    row_element = []
    for j in range(r):
        row_element.append(int(input()))
    m.append(row_element)
for i in range(r):
    for j in range(i, r):
        print(m[i][j], end = "")
    print()
