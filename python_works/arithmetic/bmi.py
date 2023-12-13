height_in_cm=int(input("Enter the height in cm: "))
weight_in_kg=int(input("Enter the weight in kg: "))

height_in_m=(height_in_cm/100)

bmi=weight_in_kg/(height_in_m**2)

print(f"BMI value is {bmi}")