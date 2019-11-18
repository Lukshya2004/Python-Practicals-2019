string = input()
prefix = input()
length = len(string)
if len(prefix)< len(string):
    if prefix in string[::length//2]:
        print("Yes")
    else:
        print("No")
else:
    if string in prefix:
        print("Your prefix is appropriate")
    else:
        print("Nope")
