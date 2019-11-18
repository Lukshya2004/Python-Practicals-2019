upper=0
lower=0
digit=0
special=0

string=input("Enter the string:")

for x in string:
    if x.isupper():
        upper+=1
    if x.islower():
        lower+=1
    if x.isdigit():
        digit+=1

special=len(string)-(upper+lower+digit)

print("upper case= ",upper,"\nlower case= ",lower,"\ndigits= ",digit,"\nspecial characters= ",special)
    

