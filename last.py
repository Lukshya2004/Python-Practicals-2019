n = int(input())
regions =[]
for i in range(n):
    x = input()
    regions.append(x)
print(regions)
final =[]
for i in regions:
    if i[0] == "N" or i[0] == "n":
        final.append(i)
    else:
        continue
print(final)
