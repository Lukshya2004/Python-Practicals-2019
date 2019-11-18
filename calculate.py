num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operator=(input("Enter any operator:"))
if (operator=="+"):
    sum=num1+num2
    print("The sum is ",sum)
elif (operator=="-"):
    diff=num1-num2
    print("The difference is ",diff)
elif (operator=="*"):
    product=num1*num2
    print("The product is ",product)
elif (operator=="/"):
    div=num1/num2
    print("The quotient is ",div)
elif (operator=="**"):
    expo=num1**num2
    print("The exponentiated form is ",expo)
else:
    print("Error")
    
