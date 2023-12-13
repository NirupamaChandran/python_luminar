from re import*
f=open("C:\\Users\\HP\\Desktop\\Pythonlmnr\\regular_expression\\vehicle_numbers.txt","r")

rule="(TN|KL)-[0-9]{2}-[A-Z]{1,2}-[0-9]{4}"

for line in f:
    veh_num=line.rstrip("\n")
    matcher=fullmatch(rule,veh_num)
    if matcher!=None:
        print(veh_num)