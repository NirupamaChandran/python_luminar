lis1=["red","green","blue","violet","black"]
lis2=["white","black","green","pink","yellow","aqua"]
print(f"list 1 is {lis1}")
print(f"list 2 is {lis2}")
common_lis=[]
for i in lis1:
    if i in lis2:
        common_lis.append(i)
print(f"common element list is {common_lis}")