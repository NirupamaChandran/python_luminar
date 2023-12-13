from re import*
date=input("enter date dd: ")
rule="(0[1-9]|[12][0-9]|3[01])"
matcher=fullmatch(rule,date)
print("invalid" if matcher==None else "valid")