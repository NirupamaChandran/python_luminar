text="pneumonoultramicroscopicsilicovolcanoconiosis"
# vow_count=0
cons_count=0

for ch in text:
    # if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    # if ch in ["a","e","i","o","u"]:
    #     vow_count+=1
    # else:
    #     cons_count+=1

    if ch not in ["a","e","i","o","u"]:
        cons_count+=1

# print(f"vowels count is {vow_count}")
print(f"consonants count is {cons_count}")
print(f"total character count is {len(text)}")