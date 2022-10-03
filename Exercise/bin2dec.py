while True:
  number = input("Enter a number that you want to convert: ")
  if number.isdigit():
    break
  else:
    print("You entered number that invalid. Please try again!")
deneme = 0
for a in range(0,2):
  for b in range(0,2):
    for c in range(0,2):
        for d in range(0,2):
            for e in range(0,2):
                deneme = e*((2)**0)+ d*((2)**1)+ c*((2)**2)+b*((2)**3)+a*((2)**4)
                if deneme == int(number):
                    print("{}{}{}{}{}".format(a,b,c,d,e))
            