from json import load
f=open("C:\\Users\\HP\\Desktop\\Pythonlmnr\\json_work\\students.json","r")
data=load(f)

print(data)

all_names=[emp.get("name") for emp in data]
print(all_names)
dept={emp.get("department") for emp in data}
print(dept)

max_sal=max(data,key=lambda d:d.get("salary"))
print(max_sal.get("name"))

