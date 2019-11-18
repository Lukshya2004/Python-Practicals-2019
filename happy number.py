#happy number- sum of squares of digit~ sum of squares of new digit~finally equal to one

print("program to check whether a number is a happy number")
#X=int(input("Enter:"))
#for N in range(1,X+1):
N=int(input("Enter the number:"))
OG_N=N
h=0
List=[ ]
while h != 1:
    while N != 0:
        R= N%10
        h=h+ R**2
        N=N//10
    
    if h ==1:
        print(OG_N , "is a happy number.")
        break
    else:
        if h in List:
            print(OG_N, "is not a happy number")
            break
        else:
            List.append(h)
            N=h
            h=0

    
        
    
