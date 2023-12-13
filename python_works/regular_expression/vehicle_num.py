from re import*
vehicle_number_rule="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"
veh_num=input("enter vehicle number: ")

matcher=fullmatch(vehicle_number_rule,veh_num)
print("invalid" if matcher==None else "valid")