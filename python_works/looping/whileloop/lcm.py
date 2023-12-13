num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

sm_num=num1 if num1<num2 else num2
gcd=1
i=1
while i<=sm_num:
    if num1%i==0 and num2%i==0:
        gcd=i
    i+=1
print(f"gcd is {gcd}")

lcm=(num1*num2)/gcd
print(f"lcm is {lcm}")