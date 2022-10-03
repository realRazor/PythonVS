try:  #  try bloğu herhangi bir error alındığında kullanıcıya bu hatayı  
      # bir mesaj ile göstermek için except bloğunu çalıştırır.
  while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if a == b:
      print("You can't enter numbers that are equals")
    elif  a >0 and b>0: # iki sayı da pozitif ise döngüyü kır. Ve devam et.
      break
    else:
      print("You can't enter any negative numbers! Please try again.")
  if a > b:
    a,b = b,a  
  
  armstrongs = []
  sum = 0


  for number in range(int(a),int(b)+1): # iki sayı arası armstrong kontrolü
    for i in str(number): # sıradaki sayının armstrong kontrolü     
        sum += int(i) ** len(str(number))
    if sum == number:
      armstrongs.append(number) # sayı armstrong ise listeye ekle
    sum=0

  
  if len(armstrongs) == 0:
    print(f"There are no Armstrong numbers between {a} and {b}.")
  else:
    print(f"The list of Armstrong numbers between {a} and {b} are as follows: {armstrongs}")
except:
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
print("CodumuCoders Team was here")