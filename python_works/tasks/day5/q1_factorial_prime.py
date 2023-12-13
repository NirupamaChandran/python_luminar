num=int(input("enter the number:"))
fact=1
is_prime=True
for i in range(2,num):
    if num%i==0:
        is_prime=False
        print("it is not a prime number")
        break
if is_prime==True:
    i=1
    while i<=num:
        fact=fact*i
        i+=1
    print(fact)