fibonacci_list = [1,1]

# for i in range(8):
#     new = fibonacci_list[i]+fibonacci_list[i+1]
#     fibonacci_list.append(new)
# print(fibonacci_list)
while True:   
    new = fibonacci_list[-1]+fibonacci_list[-2]
    fibonacci_list.append(new)
    if fibonacci_list[-1] == 55:
        break
print(fibonacci_list)
