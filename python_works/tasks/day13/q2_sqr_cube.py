sqr=[]
cube=[]
for i in range(0,10):
    num=int(input("enter number: "))
    sqr.append(num**2)
    cube.append(num**3)
print(f"square list is {sqr}")
print(f"cube list is {cube}")