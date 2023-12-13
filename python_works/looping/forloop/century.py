starting_year=int(input("Enter the staring year: "))
current_year=2024
for year in range(starting_year,current_year):
    if year%100==0:
        print(year)
