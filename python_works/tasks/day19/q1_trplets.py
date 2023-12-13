array_lst=[1,-2,3,4,-5,6,7,8,-9,-10]
triplelet_list=[]
c=0
triplelet_set=set()
for i in array_lst: 
    for k in array_lst:
        t=-(i+k)
        if t in array_lst:
            temp_list=[i,k,t]
            temp_list.sort()
            while temp_list not in triplelet_list:
                triplelet_list. append(list())
                triplelet_list[c].append (i)
                triplelet_list[c].append (k)
                triplelet_list[c].append (t)
                triplelet_list[c].sort()
                c+=1
print(f"the triplets whose sum is zero are {triplelet_list}")