#sort 3 numbers

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))


if (num1>num2 and num1>num3):
    if (num2>num3):
        print(f"sorted numbers in descending order is {num1} {num2} {num3}")
    else:
        print(f"sorted numbers in descending order is {num1} {num3} {num2}")
elif (num2>num1 and num2>num3):
    if (num1>num3):
        print(f"sorted numbers in descending order is {num2} {num1} {num3}")
    else:
        print(f"sorted numbers in descending order is {num2} {num3} {num1}")
elif (num3>num1 and num3>num2):
    if (num1>num2):
        print(f"sorted numbers in descending order is {num3} {num1} {num2}")
    else:
        print(f"sorted numbers in descending order is {num3} {num2} {num1}")
elif (num1==num2==num3):
    print("all numbers are equal")