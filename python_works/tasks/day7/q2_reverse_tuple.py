tp=("red","green","blue")
rev=[]
for i in range(len(tp)-1,-1,-1):
    rev.append(tp[i])
new_tp=tuple(rev)
print(new_tp)