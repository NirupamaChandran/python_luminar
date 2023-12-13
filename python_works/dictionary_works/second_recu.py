text="ABCABD"
chara_count={}
duplicate_chara=[]
for ch in text:
    if ch  in chara_count:
        chara_count[ch]+=1
        duplicate_chara.append(ch)
    else:
        chara_count[ch]=1
        
print(duplicate_chara[1])