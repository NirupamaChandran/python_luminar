from re import*
ph_number=input("enter phone number: ")

rule="([+]91)?[0-9]{10}"
matcher=fullmatch(rule,ph_number)
print("invalid" if matcher==None else "valid")