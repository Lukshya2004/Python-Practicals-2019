#prime nos (1-100)

X=int(input("the prime numbers between 1 and "))

if X==2:
    print(2)
elif X==3:
    print('2\n3')
elif X>3:
    print('2\n3')
    for N in range(4,X+1):
        if N==2:
            print(2,"is a prime number.")
        else:
            for k in range(2,N//2+1,1):
                if N%k == 0:
                    break
                else:
                    continue
        if k==N//2 and N%k!=0:
            print(N)
            
            
