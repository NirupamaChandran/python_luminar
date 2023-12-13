present_reading=int(input("Enter prensent reading in kwh: "))
last_reading=int(input("Enter last reading in kwh: "))

consumed_unit=present_reading-last_reading
unit_rate=int(input("Enter unit rate: "))
electricity_bill_amount=consumed_unit*unit_rate
print(f"The electricity bill amount is {electricity_bill_amount}")