text="ABCABBDE"
chara_count={}
for ch in text:
    if ch in chara_count:
        print(ch)
        break
    else:
        chara_count[ch]=1

