mobile={"id":100,"name":"iphone15","price":100000,"imei":2345,"processor":"apple"}

for k,v in mobile.items():
    print(k,v)

print(mobile.get("name"))
print(mobile.get("price"))

# mobile["price"]=85000
mobile.update({"price":85000})
print(mobile)

mobile.pop("imei")
print(mobile)

mobile.update({"offer":1000})       # add new key value pair
# mobile["offer"]=1000
print(mobile)

mobile["price"]+=1000
print(mobile)

print("color" in mobile)
print("id" in mobile)