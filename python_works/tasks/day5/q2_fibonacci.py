limit=int(input("enter the limit: "))
prev=0
curr=1
print(f"{prev} Zero")
print(f"{curr} Odd")
for i in range(1,limit):
    next=prev+curr
    if next%2==0:
        print(f"{next} Even")
    else:
        print(f"{next} Odd")
    prev=curr
    curr=next