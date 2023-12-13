nums=[12,67,5,8]
str_nums=[str(n) for n in nums]
print(str_nums)
str_nums.sort(reverse=True)
print(str_nums)



# largest number
# lst=[23,12,78,9]
# 9782312

lst=[23,12,78,9]
str_lst=[str(n) for n in lst]
str_lst.sort(reverse=True)
print(str_lst)

i=0
res=0
while(i<len(lst)):
    curr=str_lst[i]
    res=int(str(res)+curr)
    i+=1
print(res)





















# lst=[23,12,78,9]
# lst.sort(reverse=True)
# print(lst)
# i=0
# max_val=0
# while(i<len(lst)):
#     cur_max=max(lst)
#     max_val=int(str(max_val)+str(cur_max))
#     lst.remove(cur_max)
# print(max_val)