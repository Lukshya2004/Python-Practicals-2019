number = int(input())
while number != 0:
    sum1 = 0
    t = number
    while t != 0:
        r = t % 10
        sum1 += r**2
        t = t // 10
    if sum1 == 1:
        print("yers")
        break
    elif sum1 > 1 and sum1 < 9:
        print("Imma yeet you out")
        break
    else:
        number = sum1
        continue
