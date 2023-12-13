#2
lower=int(input("enter lower range: "))
upper=int(input("enter upper range: "))
sum=0
for i in range(lower,upper+1):
    if i%2==0:
        sum=sum+i
print(sum)