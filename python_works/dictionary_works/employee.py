employee={"id":1000,"name":"hari","department":"developer"}

employee["department"]="senior developer"

if "salary" not in employee:
    employee["salary"]=450000
else:
    employee["salary"]+=10000
print(employee)