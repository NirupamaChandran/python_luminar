num=int(input("enter a number with in range 20 to 30: "))
is_range=True
while is_range==True:
    if 20<=num<=30:
        print("number with in range")
        break
    else:
        num=int(input("enter the correct number: "))