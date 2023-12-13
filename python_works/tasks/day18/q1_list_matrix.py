orginal_list=[1,3,5,1,3,2,5,4,2]
new_list=[]
matrix_list=[]
count=0
for i in orginal_list:
    if i not in new_list:
        new_list.append(i)
for i in new_list:
    if orginal_list.count(i)==2:
        matrix_list.append(list())
        matrix_list[count].append(i)
        matrix_list[count].append(i)
        count+=1
    elif orginal_list.count(i)==1:
        matrix_list.append(list())
        matrix_list[count].append(i)
        count+=1
matrix_list.sort()
print(matrix_list)








