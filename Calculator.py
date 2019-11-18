print("ADDITION: A")
print("SUBTRACTION: S")
print("MULTIPLICATION: M")
print("DIVISION: D")
print("MODULUS: R")
print("QUIT: Q")
x=input("Enter the operation:")
if (x=='Q') or (x=="q"):
    quit()
else:
    if (x=='A') or (x=='a'):
        p=int(input("Enter the first number:"))
        q=int(input("Enter the first number:"))
        t=p+q
        print("The sum is", t)
    elif (x=='S') or (x=='s'):
        p=int(input("Enter the first number:"))
        q=int(input("Enter the first number:"))
        t=p-q
        print("The difference is", t)
    elif (x=='M') or (x=='m'):
        p=int(input("Enter the first number:"))
        q=int(input("Enter the first number:"))
        t=p*q
        print("The product is", t)
    elif (x=='D') or (x=='d'):
        p=int(input("Enter the first number:"))
        q=int(input("Enter the first number:"))
        t=p/q
        print("The quotient is", t)
    elif (x=='R') or (x=='r'):
        p=int(input("Enter the first number:"))
        q=int(input("Enter the first number:"))
        t=p%q
        print("The remainder is", t)
    else:
        print("invalid entry")
