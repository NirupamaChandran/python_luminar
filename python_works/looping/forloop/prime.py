num=int(input("Enter the number: "))
is_prime=True
for i in range(2,num):
    if num%i==0:
        is_prime=False
        break
print(is_prime)

