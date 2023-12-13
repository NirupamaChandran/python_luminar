#anagram

source_word="won"
target_word="now"

sw=sorted(source_word)
tw=sorted(target_word)
print(f"True" if sw==tw else "False")