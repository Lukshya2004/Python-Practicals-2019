X=list()
Y=list()
Z=list()
M=int(input("Enter size of X:"))
N=int(input("Enter size of Y:"))
for q in range(M):
    xelement=int(input("Enter elements of X:"))
    X.append(xelement)
for q in range(M):
    yelement=int(input("Enter elements of Y:"))
    Y.append(yelement)
print("X=",X)
print("Y=",Y)
# (i)
for x in X:
    if x%2==0:
        
