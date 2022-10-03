
def StringChallenge(string):
    sum = 0
    sum2 = 0
    for i in string:
        if i.isdigit():
            if not string[string.index(i)+1].isdigit():
                if string.count(i) >= 1:
                    sum += int(i)
        if i.isalpha():
            sum2 += 1
    result = round(sum/sum2)
    return result
print(StringChallenge("H3ello9-9"))
