from re import *

text="fat-cat-run-fast-catch"
pattern="at"
matcher=finditer(pattern,text)

at_count=0
for m in matcher:
    print(m.start(),m.group())
    at_count+=1
print(at_count)

