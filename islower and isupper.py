line=input("enter a line:")
lowercount = uppercount = 0
digitcount = alphacount = 0
for a in line:
    if a.islower():
        lowercount+=1
    elif a.isupper():
        uppercount+=1
    elif a.isalpha():
        alphacount+=1
    elif a.isdigit():
        digitcount+=1
print("Number of uppercase letters:", uppercount)
print("Number of lowercase letters:", lowercount)
print("Number of alphabets:", alphacount)
print("Number ofdigits:", digitcount)
