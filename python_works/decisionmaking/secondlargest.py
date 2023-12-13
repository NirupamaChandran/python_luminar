num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

# if (num1>num2>num3 or num3>num2>num1):
#     print(f"second largest number is {num2}")
# elif (num2>num1>num3 or num3>num1>num2):
#     print(f"second largest number is {num1}")
# elif (num2>num3>num1 or num1>num3>num2):
#     print(f"second largest number is {num3}")
# elif (num1==num2==num3):
#     print("all numbers are equal")


if (num1>num2 and num1>num3):
    if (num2>num3):
        print(f"second largest number is {num2}")
    else:
        print(f"second largest number is {num3}")
elif (num2>num1 and num2>num3):
    if (num1>num3):
        print(f"second largest number is {num1}")
    else:
        print(f"second largest number is {num3}")
elif (num3>num1 and num3>num2):
    if (num1>num2):
        print(f"second largest number is {num1}")
    else:
        print(f"second largest number is {num2}")
elif (num1==num2==num3):
    print("all numbers are equal")
