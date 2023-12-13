# lst=[] empty list
# list() empty list
orders=["friedrice","gheerost","vb","cb","bb","cb","vb","cb"]
#                                    -4   -3   -2   -1

orders.append("tea")  #append to last of the list
print(orders)

print(orders.count("cb"))

print(orders.index("gheerost"))

print(orders.pop(1)) #pop(index=-1) default.
print(orders)       #we can use negative indexing in list

orders.insert(1,"goby") #insert(index,obj)
print(orders)

orders.remove("vb")
print(orders)

new_order=orders.copy()
new_order.remove("friedrice")
print(new_order)

orders.reverse()
print(orders)

new_order.sort(reverse=True) #sort() only for list. it is a method of class list. (sorted is a function).
print(new_order)