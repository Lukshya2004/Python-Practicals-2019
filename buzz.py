#buzz
K=int(input("ENTER:"))
for N in range(K + 1):
    if N%7==0:
        print("BUZZ")
    elif N%10==7:
        print("BUZZ")
    elif (N <= 79) and (N>=70):
        print("BUZZ")
    else:
        print(N)
