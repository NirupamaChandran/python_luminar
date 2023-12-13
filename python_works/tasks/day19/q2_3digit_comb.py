num_set=set()
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            num=i*100+j*10+k
            num_set.add(num)
print(num_set)