PASSWORD = input()
length = len(PASSWORD)
if PASSWORD[0].isdigit() and (length > 6 or length == 6) :
    print("YES")
else:
    print("No")
