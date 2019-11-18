number = int(input())
while number != 0:
    sum1 = 0
    a = number
    while a != 0:
        r = a % 10
        sum1 += (r**2)
        a = a // 10
    if sum1 == 1:
        print("Happy number ")
        break
    elif sum1 > 1 and sum1 < 9 :
        print("Not a happy number")
        break
    else:
        number = sum1
        continue
