unit_cons=int(input("enter the number of units consumed: "))
if unit_cons<=100:
    print("No Charge")
elif unit_cons<=200:
    rate=(unit_cons-100)*5
    print(f"your electricity bill is {rate}")
elif unit_cons>200:
    rate=(unit_cons-200)*10+500
    print(f"your electricity bill is {rate}")