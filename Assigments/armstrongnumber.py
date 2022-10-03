try:
      number = input("Please enter a number: ")
      digit_number = len(number)
      new_number = 0
      
      for i in number:
        new_number += pow(int(i),digit_number)
      if new_number == int(number):
        print(f"{number} is an Armstrong number")
        
      else:
        print(f"{number} is not an Armstrong number")
        
except:
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
# ```
# other solution:
#num = input("Please enter a number: ")
#sum = 0
#length = len(num)
#count = 0
#if num.isdigit():  
#  while count < length:
#    sum += pow(int(num[count]),length)
#    count += 1
#  if int(num) == sum:
#    print(f"{num} is an Armstrong number")
#  else:
#    print(f"{num} is not an Armstrong number")
#else:
#  print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")
 # ```