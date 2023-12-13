# find common elements

# list1=[9,4,3,10,15]
# list2=[5,4,2,3,20]
# for num in list1:
#     if num in list2:
#         print(num)


list1=[9,4,3,10,15]
list2=[5,4,2,3,20]
list1.sort()
list2.sort()
p1,p2=0,0
while(p1<len(list1) and p2<len(list2)):
    if list1[p1]==list2[p2]:
        print(list1[p1])
        p1+=1
        p2+=1
    elif list1[p1]<list2[p2]:
        p1+=1
    elif list1[p1]>list2[p2]:
        p2+=1