lst=[10,2,11,5,7,20]
search_element=int(input("Enter number: "))
is_present=False
i=0
while i<len(lst):
    cur_element=lst[i]
    if cur_element==search_element:
        is_present=True
        break
    i+=1
print(is_present)