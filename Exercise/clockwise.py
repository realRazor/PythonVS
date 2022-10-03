list1 = [
[ 13, 14, 15, 16, 1],
[ 12, 23, 24, 17, 2],
[ 11, 22 ,25, 18, 3],
[ 10, 21, 20, 19, 4],
[  9,  8,  7,  6, 5]
]
newlist=[]
for i in range(round(len(list1)/2)):
    for i in range(len(list1[0])):
        newlist.append(list1[i][len(list1)-1])
        del list1[i][len(list1)-1]
    for i in range(len(list1[0])):
        newlist.append(list1[len(list1)-1][len(list1[i])-i-1])
        del list1[len(list1)-1][len(list1[i])-i-1]
    else:
        del list1[len(list1)-1]
    for i in range(len(list1[0])):
        newlist.append(list1[len(list1)-i-1][0])
        del list1[len(list1)-i-1][0]
    for i in range(len(list1[0])):
        newlist.append(list1[0][0])
        del list1[0][0]
    else:
        del list1[0]
newlist.append(list1[0][0])
print(newlist)