# +, -, *, /, %,  //, **

num1=10
num2=10

add_res=num1+num2
sub_res=num1-num2
mul_res=num1*num2
div_res=num1/num2
exp_res=num1**num2
floor_res=num1//4 #remove value after point

print(f"addition result num1+num2={add_res}")
print(f"subtraction result num1-num2={sub_res}")
print(f"multiplication result num1*num2={mul_res}")
print(f"division result num1/num2={div_res}")
print(f"exponent result num1**num2={exp_res}")
print(f"floor division result num1//4={floor_res}")

num1 +=50
print(num1)