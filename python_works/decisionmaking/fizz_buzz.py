num=int(input("Enter the number: "))

if num%15==0:
    print("fizzbuzz")

elif num%5==0:
    print("buzz")

elif num%3==0:
    print("fizz")

else:
    print("Not divisible by 3, 5 and 15")