height=float(input("enter height in cm: "))
weight=float(input("enter weight in kg: "))

height_in_m=height/100
bmi=weight/(height_in_m**2)
print("you are under weight" if bmi<=19 else "you are healthy" if bmi<=25 else "you are over weight")