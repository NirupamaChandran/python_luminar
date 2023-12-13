height_in_cm=int(input("Enter the height in cm: "))
weight_in_kg=int(input("Enter the weight in kg: "))

height_in_m=(height_in_cm/100)

bmi=weight_in_kg/(height_in_m**2)

print(f"BMI value is {bmi}")

# if bmi<=19:
#     print("you are under weight")
# elif 19<bmi<=25:
#     print("you are healthy")
# elif 25<bmi<=30:
#     print("you are over weight")
# elif 30<bmi<=40:
#     print("you are obesity")
# else:
#     print("you are severe obese")

if bmi<=19:
    print("you are under weight")
elif bmi<=25:
    print("you are healthy")
elif bmi<=30:
    print("you are over weight")
elif bmi<=40:
    print("you are obesity")
else:
    print("you are severe obese")