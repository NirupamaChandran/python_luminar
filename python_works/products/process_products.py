from json import load
f=open("C:\\Users\\HP\\Desktop\\Pythonlmnr\\products\\items.json","r",encoding="utf-8")
data=load(f)

print(len(data))

category={p.get("category") for p in data}
print(category)

electronics=[p for p in data if p.get("category")=="electronics"]
print(len(electronics))

jewelery=[p for p in data if p.get("category")=="jewelery"]
print(len(jewelery))

costly_products=max(data,key=lambda p:p.get("price"))
print(costly_products.get("title"))