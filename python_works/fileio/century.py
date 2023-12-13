# path="C:\\Users\\HP\\Desktop\\Pythonlmnr\\fileio\\century_years.txt"
# f=open(path,"w")

# starting_year=1800
# current_year=2025
# for year in range(starting_year,current_year):
#     if year%100==0:
#         f.write(str(year)+"\n")

# path="C:\\Users\\HP\\Desktop\\Pythonlmnr\\fileio\\years.txt"
# f=open(path,"w")
# for year in range(1800,2025):
#     f.write(str(year)+"\n")

read_path="C:\\Users\\HP\\Desktop\\Pythonlmnr\\fileio\\years.txt"
write_path="C:\\Users\\HP\\Desktop\\Pythonlmnr\\fileio\\leap_years.txt"

fr=open(read_path,"r")
fw=open(write_path,"w")

for line in fr:
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        fw.write(str(year)+"\n")