from json import load
f=open("C:\\Users\\HP\\Desktop\\Pythonlmnr\\currency_exchange\\currency_data.json",encoding="utf-8")
data=load(f)

source_currency_code=input("enter source currency code: ")
target_currency_code=input("enter target currency code: ")
amount=int(input("enter amount: "))

conversion_rates=data.get("conversion_rates")
print(conversion_rates)

source_currency_code_rate=conversion_rates.get(source_currency_code)
target_currency_code_rate=conversion_rates.get(target_currency_code)
print(source_currency_code_rate)
print(target_currency_code_rate)

result=(amount/source_currency_code_rate)*target_currency_code_rate
print(result)