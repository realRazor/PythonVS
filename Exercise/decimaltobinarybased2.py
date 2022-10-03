user =input("pls enter a decimal number: ")
bin=""
decimal=int(user)

while int(decimal)>0:
    bin=bin+str(decimal%2)
    decimal=int(decimal/2)
   
print(bin[::-1])