product={"code":1001,"name":"orange","price":35}

for k in product.keys():
    print(k)                # keys() return all keys in a dictionary

for v in product.values():
    print(v)                # values return all values in a dictionary

for k,v in product.items():
    print(k,v)              # items() return all key value pairs in a dictionary

# print(product["pricess"])         # shows error
print(product.get("pricess"))       # get() shows none

product["price"]=50                 # update
print(product)
product.update({"name":"oranges"})  # update() method
print(product)

product.pop("price")                # remove key va;ue pair
print(product)

