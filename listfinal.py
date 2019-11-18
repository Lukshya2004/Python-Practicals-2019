l =[]
l1 = []
while True:
    x = input()
    y = int(input())
    l.append(y)
    l1.append(x)
    if x = "zzz" and y = "9999":
        break
print(l,l1)
count = 0
country = input()
for i in range(len(l)):
    if country == l1[i]:
        print(l[i])
    else:
        count+=1
        if count == len(l1):
            print("not found")
            break            
