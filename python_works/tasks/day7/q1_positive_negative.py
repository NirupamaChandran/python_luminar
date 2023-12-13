num_lis=[-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9]
positive=[]
negative=[]
for num in num_lis:
    if num<0:
        negative.append(num)
    else:
        positive.append(num)
print(f"positive numbers {positive}")
print(f"negative numbers {negative}")