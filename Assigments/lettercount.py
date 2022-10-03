
dic_word = {}
a = ""
def StringChallange(str):
    for i in str:
        if i.isalpha():
            a = str.count(i)
            dic_word.update({i:a})

    for i in dic_word.keys():
        a += str(dic_word[i]+str(i))
print(StringChallange("AABBBCCDDD"))