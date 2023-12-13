# starting with k,l,m or n
# second place must be digit that is divisible by 3
# followed by any number of alphabets and numbers

from re import*
rule="[k-nK-N][369][a-zA-Z0-9]*"
text=input("enter text: ")
matcher=fullmatch(rule,text)
print("invalid" if matcher==None else "valid")