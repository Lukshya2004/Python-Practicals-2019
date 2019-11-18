n = int(input())
regions =[]
for i in range(n):
    x = input()
    regions.append(x)
print(regions)
final =[]
for i in regions:
    length = len(i)
    if len(i) <= 5:
        final.append(i)
    else:
        continue
print(final)
