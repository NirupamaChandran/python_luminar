# text="hello hai hello hai"
# word count

text="hello hai hello hai"
txt_split=text.split()
print(txt_split)
word_count={}
for w in txt_split:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)


