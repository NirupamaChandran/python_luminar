year=int(input("enter year: "))
print(f"{year} is a leap year" if year%100==0 and year%400==0 or year%100!=0 and year%4==0 else "it is not a leap year")