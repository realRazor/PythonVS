# -2 tabanlı decimal to binary
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
          for f in range(0,2):
            for g in range(0,2):
              for x in range(0,2):
                for y in range(0,2):
                  for z in range(0,2):
                    deneme = z*((-2)**0)+ y*((-2)**1)+ x*((-2)**2)+g*((-2)**3)+f*((-2)**4)+e*((-2)**5)+d*((-2)**6)+c*((-2)**7)+b*((-2)**8)+a*((-2)**9)
                    if deneme == int(number):
                      print("{}{}{}{}{}{}{}{}{}{}".format(a,b,c,d,e,f,g,x,y,z).lstrip("0"))
                      