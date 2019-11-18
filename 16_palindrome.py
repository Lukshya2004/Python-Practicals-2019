 #palindrome
string=input("Enter your string:")
reverse=""
for y in range(-1, (len(string)+1)*-1, -1):
    x=string[y]
    reverse = reverse + x
if string==reverse:
    print(string, "is a palindrome")
    
    
