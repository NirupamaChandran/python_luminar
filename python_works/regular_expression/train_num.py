from re import*
f=open("C:\\Users\\HP\\Desktop\\Pythonlmnr\\regular_expression\\train.txt","r")
rule="[0-9]{5}"
for line in f:
    train_num=line.rstrip("\n")
    matcher=finditer(rule,train_num)
    for m in matcher:
        print(m.group())





# for line in f:
#     train_num=line.rstrip("\n").split(" ")
#     for t in train_num:
#         matcher=fullmatch(rule,t)
#         if matcher!=None:
#             print(t)