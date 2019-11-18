num1 = int(input())
while num1 != 0:
    sum1 = 0
    a = num1
    while a != 0:
        r = a % 10
        sum1 += r
        a = a // 10
    if sum1 == 1:
        print("Magic Number")
        break
    elif sum1 > 1 and sum1 < 9:
        print("Nope")
        break
    else:
        num1 = sum1
        continue
