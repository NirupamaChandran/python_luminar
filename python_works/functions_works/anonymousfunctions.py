# lambda used when there is only one line in function

cube=lambda n:n**3
print(cube(2))

max_two=lambda n1,n2:n1 if n1>n2 else n2
print(max_two(20,100))

num_chk=lambda n:"positive" if n>0 else "negative" if n<0 else "zero"
print(num_chk(5))

odd_even=lambda n:"odd" if n%2!=0 else "even"
print(odd_even(4))

text="good evening all"
words=text.split(" ")
srt_words=sorted(words,key=lambda w:len(w),reverse=True)
print(srt_words)