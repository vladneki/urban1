def single_root_words(root_word, *other_words):
    word = str(root_word).lower()
    same_words = []
    for i in other_words:
        i = str(i).lower()
        if word in i or i in word:
            same_words.append(i)
    return same_words

result = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result)
print(result2)