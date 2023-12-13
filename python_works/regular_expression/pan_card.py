from re import*
pan_text=input("enter pan card number: ")
rule="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]"
matcher=fullmatch(rule,pan_text)
print("invalid" if matcher==None else "valid")