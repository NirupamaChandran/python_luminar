text=input("enter the string: ")
is_paliandrome=True
i=0
j=len(text)-1
while i<j:
    if text[i]!=text[j]:
        is_paliandrome=False
        break
    i+=1
    j-=1
print(f"{text} is paliandrome" if is_paliandrome else "Not a paliandrome")