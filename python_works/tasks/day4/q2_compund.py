principal=int(input("enter principal amount: "))
rate_of_interest=int(input("enter rate of interest: "))
time_period=int(input("enter time period: "))
a=principal*(1+(rate_of_interest/100))**time_period
compund_interest=a-principal

print(f"compound interest for amount {principal} is {compund_interest}")