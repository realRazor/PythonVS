
# entry = input("Please enter 2 or 3 digit number to check for the closest palindrome: ").lstrip("-").lstrip("0")

# if len(entry) == 3:  # 185
  
#   first_number = entry[:2]+entry[0]
#   a = str(int(entry[1])+1)                                                                  
#   second_number = entry[0]+a+entry[0]
#   diff1= int(entry)-int(first_number)
#   diff2 = int(second_number)-int(entry)
  
#   if diff1 > diff2:
#       print(second_number)
#   elif diff1 == diff2:
#     print(first_number,second_number)
#   else:
#       print(f"{first_number}") 

# elif len(entry) == 2:
#   first_n = entry[0]*2
#   second_n = str(int(entry[0])-1)*2
#   third_n = str(int(entry[0])+1)*2
#   a = int(entry) - int(second_n)  
#   b = int(third_n) - int(entry)
#   c = int(first_n) - int(entry)
#   if min(a,b,c) == a:
#     print(second_n)
#   elif min(a,b,c) == b:
#     print(third_n)
#   else:
#     print(first_n)
def ispalindrome(i):
  
  if i == i[::-1]:
    return True
  else:
    return False
num1 = input("Brinci sayı: ")
num2 = input("İkinci sayı: ")
pal_list = []

if int(num1)>int(num2):
  num1,num2 = num2,num1
for i in range(int(num1),int(num2)+1):
  if ispalindrome(str(i)):
    pal_list.append(i)
print(pal_list)