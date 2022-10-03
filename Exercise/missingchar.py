def missing_char(word, n):
    newword = word.replace(word[n],"")
    return newword
print(missing_char("kitchen",4))