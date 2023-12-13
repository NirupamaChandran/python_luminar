num=input("Enter the number: ")
digit_count=len(num)
num=int(num)
number=num
sum=0

while num!=0:
    digit=num%10
    exp=digit**digit_count
    sum=sum+exp
    num=num//10
print(sum)
print("armstrong" if sum==number else "not armstrong")