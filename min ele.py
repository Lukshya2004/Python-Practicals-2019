lst=eval(input("Enterlist:"))
length=len(lst)
min_ele=lst[0]
min_index=0
for i in range(1,length-1):
    if lst[i]<min_ele:
        min_ele=lst[i]
        min_index=i
print("Given list is :",list)
print("The minimim element of the given list:")
print(min_ele, "at index",min_index)
