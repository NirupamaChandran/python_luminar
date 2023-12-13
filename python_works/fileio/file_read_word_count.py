f=open("C:\\Users\\HP\\Desktop\\Pythonlmnr\\fileio\\data2.txt","r")
total_word_count=0
wc={}
for line in f:
    words=line.rstrip("\n").split()
    print(words)
    total_word_count=total_word_count+len(words)
    for w in words:
        if w in wc:
            wc[w]+=1
        else:
            wc[w]=1
# word count
print(wc)

# total number of words
print(total_word_count)
