num=int(input("enter a decimal number number:"))
orginal=num
binary=""
if num==0:
    binary=0
else:
    while num>0:
        mod=num%2
        binary=str(mod)+binary
        num=num//2
print(f"binary of {orginal} is {binary}")
