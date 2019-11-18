string=input("Enter your string:")
A,E,I,O,U=0,0,0,0,0
#string="awerty"
for x in string:
    if x=="A" or x == "a":
        A=A+1
    elif x=="E" or x=="e":
        E=E+1
    elif x=="I" or x =="i":
        I=I+1
    elif x=="O" or x=="o":
        O=O+1
    elif x=="U" or x =="u":
        U=U+1
print("A",end="")
for k in range(A):
    print("\t", "#", end="")
print()

print("E",end="")
for k in range(E):
    print("\t", "#", end="")
print()

print("I",end="")
for k in range(I):
    print( "\t", "#", end="")
print()

print("O",end="")
for k in range(O):
    print("\t", "#", end="")
print()

print("U",end="")
for k in range(U):
    print("\t", "#", end="")
print()

#end
          
