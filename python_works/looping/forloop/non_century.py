starting_year=int(input("Enter the staring year: "))
current_year=2023
for year in range(starting_year,current_year+1):
    if year%100!=0:
        print(year)