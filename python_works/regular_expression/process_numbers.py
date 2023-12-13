from re import*
f=open("C:\\Users\\HP\\Desktop\\Pythonlmnr\\regular_expression\\numbers.txt","r")
rule="([+]91)?[0-9]{10}"

for line in f:
    numbers=line.rstrip("\n")
    matcher=fullmatch(rule,numbers)
    if matcher!=None:
        print(numbers)