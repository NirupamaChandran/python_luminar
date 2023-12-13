expenses=[12000,13000,23000,24000,25000,32000,23000]

# for i in range(0,len(expenses)):
#     print(expenses[i])

# for exp in expenses:
#     print(exp)

# for i in range(0,len(expenses)):
#     if expenses[i]>15000:
#         print(expenses[i])

# for i in range(0,len(expenses)):
#     # if expenses[i]>15000 and expenses[i]<25000:
#     if expenses[i] in range(15000,25000):
#         print(expenses[i])


# max_exp=max(expenses)
# min_exp=min(expenses)
# sum_exp=sum(expenses)

# print(max_exp)  # max min sum functions (itrable)
# print(min_exp)
# print(sum_exp)

# avg_exp=sum_exp/len(expenses)
# print(avg_exp)


items=["bat","ball","stumps","helmet","arc","cricketball"]
# longest_word=max(items,key=lambda w:len(w)) #key used when we need any customization in pyhton's default function definition
# print(longest_word)
# min_word=min(items,key=lambda w:len(w))
# print(min_word)

# max
# min
# sum

max_w=items[0]
for i in range(0,len(items)):
    current_w=items[i]
    if len(max_w)<len(current_w):
        max_w=current_w
print(max_w)

min_w=items[0]
for i in range(0,len(items)):
    curr_w=items[i]
    if len(min_w)>len(curr_w):
        min_w=curr_w
print(min_w)


sum=0
for i in range(0,len(items)):
    sum=sum+len(items[i])
print(sum)