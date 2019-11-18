l= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]
for i in range(1,2):
    for j in range(i):
        print(l[j], end ="")
        del l[j]
    print()
