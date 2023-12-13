Dengue_lis=["ekm","tsr","tvm","ekm","tvm","ekm","tvm","idk","tvm"]
wc={}
for w in Dengue_lis:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1
print(wc)
srt_wc=sorted(wc, key=lambda k:wc.get(k),reverse=True)
print(srt_wc)