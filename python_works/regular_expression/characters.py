from re import *

text="kaBczabc 9@7c"
pattern="\w"   
# [a-e] match a to e sequence
# "a"
# (ab)  a and b
# [abc] a or b or c
# [a-z]
# [A-Z]
# [a-zA-Z]
# [0-9]
# [a-zA-Z0-9]
# [^a-z] exclude a-z
# \d --- equivalent to 0-9
# \D --- exclude digits [^0-9]
# \w --- alphanumeric [a-zA-Z0-9]
# ? optional

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())