array =[
[ 13, 14, 15, 16, 1],
[ 12, 23, 24, 17, 2],
[ 11, 22 ,25, 18, 3],
[ 10, 21, 20, 19, 4],
[  9,  8,  7,  6, 5]
]
newlist = []
counter = 0

for i in range(5):
    newlist.append(array[i][-1])
    if i == 4:
        for j in range(-2,-6,-1):
            newlist.append(array[i][j])
            if j == -5:
                for k in range(3,-1,-1):
                    newlist.append(array[k][j])
                    if k == 0:
                        for l in range(-4,-1,1):
                            newlist.append(array[k][l])
                            if l == -2:
                                for m in range(1,4):
                                    newlist.append(array[m][l])
                                    if m == 3:
                                        for n in range(-3,-5,-1):
                                            newlist.append(array[m][n])
                                            if n == -4:
                                                for p in range(2,0,-1):
                                                    newlist.append(array[p][n])
                                                    if p == 1:
                                                        for r in range(1,3):
                                                            newlist.append(array[r][-3])
                                                            
print(newlist)                                            



