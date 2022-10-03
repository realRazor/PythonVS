# word = input("Enter a word: ")
# for i in range(1,len(word)+1,2):
#   print("{:^101}".format(word[:i]))
for x in range(1,101):
    if (x % 3 ==0) and (x % 5 ==0):
        print("FizzBuzz") 
    elif (x % 5 ==0): 
        print("Buzz")
    elif (x % 3 ==0):
        print("Fizz")
    else:
        print(x)