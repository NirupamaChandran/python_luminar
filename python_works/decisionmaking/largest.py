# largest among two numbers

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

if num1>num2:
    print(f"largest number is {num1}")
elif num2>num1:
    print(f"largest number is {num2}")
else:
    print(f"The numbers are equal")