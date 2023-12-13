text="ABCABBDE"
chara_count={}

for ch in text:
    if ch in chara_count:
        chara_count[ch]+=1
    else:
        chara_count[ch]=1
print(chara_count)
for k,v in chara_count.items():
    if v==1:
        print(k)