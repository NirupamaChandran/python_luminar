# 'string valid'
# "string valid"
# """string
# valid"""

#cmd python pythonshell dir() in bracket class name

# method are defined inside class. if it is outside class then it is a function
# object.method_name()


company="LUMINAR"
# print(company.casefold())     # casefold() uppercase to lower case. advanced method
print(company.lower())          # lower() convert into lowercase

name="nirupama"
print(name.capitalize())    #def capitalize() capitalize first character in string
print(name.upper())         #upper() covert into uppercase

var="niru123"
print(var.isalpha())    # isalpha() return true if only alphabets in string else false for string only
print(var.isdigit())    # isdigit() return true if all chara are numbers else false for string only
print(var.isalnum())    # isalnum() true if alphabets or numbers

comp="hello\n"
# print(comp.strip("\n"))     # strip() remove char from left or right of target char
print(comp.rstrip("\n"))
# print(comp.lstrip("h"))

my_name="nirupama chandran kanjirakadu"
print(my_name.split())