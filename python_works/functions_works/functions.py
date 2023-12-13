def add(n1,n2):
    res=n1+n2
    return res
print(f"addition result is {add(10,20)}")

def sub(n1,n2):
    res=n1-n2
    return res
print(f"subtraction result is {sub(30,10)}")

def div(n1,n2):
    res=n1/n2
    return res
print(f"division result is {div(10,2)}")

def mul(n1,n2):
    res=n1*n2
    return res
print(f"multiplication result is {mul(3,2)}")

def smart_sub(n1,n2):
    res=n1-n2 if n1>n2 else n2-n1
    return res
print(f"smart subtraction result is {smart_sub(10,50)}")

def cube(num=2):  #if there is no parameter passed while calling
    res=num**3
    return res
print(cube())

def nth_power(num,n=2):
    res=num**n
    return res
print(nth_power(5))


def oneth_smallest_num(n1,n2):
    res=n1 if n1%10<n2%10 else n2
    return res
print(oneth_smallest_num(432,18))


def century_year(year):
    res=True if year%100==0 else False
    return res
print(century_year(2023))


# leap_year
# factorial(num)
# prime(num)
# armstrong(num)


def leap_year(year):
    res=True if year%100==0 and year%400==0 or year%100!=0 and year%4==0 else False
    return res
print(leap_year(2023))

def factorial(num):
    fact=1
    for f in range(1,num+1):
        fact=fact*f
    return fact
print(factorial(5))

def prime(num):
    for i in range(2,num):
        res=False if num%i==0 else True
    return res
print(prime(11))



def armstrong(num):
    digit_count=len(num)
    num=int(num)
    number=num
    sum=0
    while num!=0:
        last_digit=num%10
        exp=last_digit**digit_count
        sum=sum+exp
        num=num//10
    res=True if number==sum else False
    return res

# num=input("Enter the number: ")
print(armstrong("153"))
