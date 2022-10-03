
def isprime(i):
    count = 0
    for x in range(2,i): 
        if i % x != 0:
            count = count
        else:
            count = 1    
    if count == 0:
        return True
    else:
        return False      
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
primelist = []
if num1>num2:
    num1,num2 = num2,num1

for i in range(num1,num2):
    if isprime(i):
        primelist.append(i)
print(primelist)