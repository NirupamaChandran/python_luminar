# arry=[1,4,3,5,6,7]
# find missing positive integer. here 2.

# sort
# diff
# if diff not 1 then mising


arr=[1,4,3,5,6,7]
arr.sort()
print(arr)
i=0
while (i<len(arr)-1):
    j=i+1
    ith_element=arr[i]
    jth_element=arr[j]
    diff=jth_element-ith_element
    if diff!=1:
        print(ith_element+1)
        break
    i+=1