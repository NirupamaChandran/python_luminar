dic={"person1":161, "person2":170, "person3":150, "person4":157, "person5":171, "person7":180}
print(dic)
print("person with height less than 170")
for k,v in dic.items():
    if dic.get(k)<170:
        print({k:v})