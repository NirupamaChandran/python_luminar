prev=0
curr=1
print(f"{prev},{curr}",end=",") # end=\n(default) for new line, # for no new line
for i in range(1,11):
    next=prev+curr
    print(next,end=",")
    prev=curr
    curr=next