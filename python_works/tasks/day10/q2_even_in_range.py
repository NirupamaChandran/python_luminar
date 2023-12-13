lower_limit=int(input("enter the lower limit: "))
upper_limit=int(input("enter the upper limit: "))
lis=[]
for i in range(lower_limit,upper_limit+1):
    if i%2==0:
        lis.append(i)
print(f"even numbers in range {lis}")
for i in lis:
    if i%5==0:
        lis.remove(i)
print(f"even numbers after deleting multiplication of 5 {lis}")

    


