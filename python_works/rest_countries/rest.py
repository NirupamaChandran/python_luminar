from json import load
f=open("C:\\Users\\HP\\Desktop\\Pythonlmnr\\rest_countries\\data.json",encoding="utf-8")
data=load(f)
print(len(data))

# all_country_names=[c.get("name") for c in data]
# print(all_country_names)

# independent_country_names=[c.get("name") for c in data if c.get("independent")==True]
# print(independent_country_names)

# all_regions={c.get("region") for c in data}
# print(all_regions)

# asian_country_names=[c.get("name") for c in data if c.get("region")=="Asia"]
# print(asian_country_names)

capital_of_ukraine=[c.get("capital") for c in data if c.get("name")=="Ukraine"]
print(capital_of_ukraine)

# country name and its capital
countries_capital=[(c.get("name"),c.get("capital")) for c in data]
print(countries_capital)

# country name and currencies
for c in data:
    if "currencies" in c:
        currency_data=c.get("currencies")[0]
        print(currency_data.get("name"),",",c.get("name"))


india_borders=[c.get("borders") for c in data if c.get("name")=="India"][0]
print(india_borders)

Indian_borders_names=[c.get("name") for c in data if c.get("alpha3Code") in india_borders]
print(Indian_borders_names)

for c in data:
    if "borders" in c and len(c.get("borders"))>4:
        print(c.get("name"))
    