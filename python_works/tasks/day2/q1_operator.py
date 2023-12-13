#1
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
operator=input("enter the operator: ")

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2 if num1>num2 else num2-num1)
elif operator=="/":
    print(num1/num2)
elif operator=="*":
    print(num1*num2)
elif operator=="//":
    print(num1//num2)
elif operator=="**":
    print(num1**num2)