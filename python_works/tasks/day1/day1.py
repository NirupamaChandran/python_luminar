#1
num=int(input("enter a number: "))
print("HELLO" if num%5==0 else "BYE")

#2
age=int(input("enter your age: "))
print("you are eligible for voting" if age>=18 else "not eligible for voting")

#3
percentage=int(input("enter your percentage: "))
print("A Grade" if percentage>90 else "B Grade" if percentage>80 else "C Grade" if percentage>=60 else "D Grade")

#4
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))
if num1>num2 and num1>num3:
    print(f"largest number is {num1}")
elif num2>1 and num2>num3:
    print(f"largest number is {num2}")
elif (num3>num1 and num3>num2):
    print(f"largest number is {num3}")
elif (num1==num2==num3):
    print("all numbers are equal")