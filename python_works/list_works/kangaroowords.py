source_word="myself"
target_word="self"

source_word_lst=[ch for ch in source_word]
target_word_lst=[ch for ch in target_word]

print(source_word_lst)
print(target_word_lst)

for ch in target_word_lst:          #if break block works then for else didn't run
    if ch in source_word_lst:
        source_word_lst.remove(ch)
    else:
        print("not a kangaroo word")
        break
else:
    print("kangarooword")