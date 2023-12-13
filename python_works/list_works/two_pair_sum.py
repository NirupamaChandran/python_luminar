#imp

# lis=[3,4,5,2,6]

# sum=int(input("Enter sum: "))         High complexity
# lis.sort()
# for i in range(0,len(lis)-1):
#     for j in range(i+1,len(lis)):
#         cur_sum=lis[i]+lis[j]
#         if cur_sum==sum:
#             print(lis[i],lis[j])
#             break

lis=[3,4,5,2,6]
lis.sort()
low=0
upp=len(lis)-1
sum=int(input("Enter sum: "))

while (low<upp):
    cur_sum=lis[low]+lis[upp]
    if cur_sum==sum:
        print(lis[low],lis[upp])
        low+=1
        upp-=1
    elif cur_sum<sum:
        low+=1
    elif cur_sum>sum:
        upp-=1




   