lst=[2,4,5,6,7,8,9]
# squares=[]
# for num in lst:
#     sq=num**2
#     squares.append(sq)
# print(squares)

# [rturn valu for num in lst condition]
squares=[num**2 for num in lst ]
print(squares)

cube=[num**3 for num in lst ]
print(cube)

# evens=[]
# for num in lst:
#     if num%2==0:
#         evens.append(num)
# print(evens)

evens=[num for num in lst if num%2==0]
print(evens)
num_gtr=[num for num in lst if num>6]
print(num_gtr)


c4=["niru","nirupama","anjitha","manoj"]
upper_names=[names.upper() for names in c4 ]
print(upper_names)
names_gtr=[names for names in c4 if len(names)>5]
print(names_gtr)

lis=["red","green","blue","white","black","apple","ignore","under"]
 
# vow=("a","e","i","o","u")
# vow_words=[words for words in lis if words.startswith(vow)]

vow_words=[w for w in lis if w[0] in ["a","e","i","o","u"]]
print(vow_words)

con_words=[words for words in lis if words not in vow_words]
print(con_words)

