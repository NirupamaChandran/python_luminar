str=input("Enter the string: ")
digit_count=0
letter_count=0
for i in str:
    if i.isalpha():
        letter_count+=1
    elif i.isdigit():
        digit_count+=1
print(f"digit count is {digit_count}")
print(f"letter count is {letter_count}")
