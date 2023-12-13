# quantifiers -----> * and {}

from re import *

text="aaabcaabbaaaabadaaaaaa"
      
pattern="a{2,4}"   
# "a*"    any number of a including zero occurrence
# "a{2}"  two a
# "a{2,4}" minimum 2 maximum 4 a


matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start(),m.group())
#     count+=1
# print(count)