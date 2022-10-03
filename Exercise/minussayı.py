from stat import SF_APPEND


while True:
  a = int(input("Enter first number: "))
  b = int(input("Enter second number: "))
  if (a == b or a<0 or b<0):
    print("Hatalı girdiniz tekrar deneyin")
  else:
    break

if a<b:
  a,b = b,a
  
def minus(a,b):
  return a - b
print(minus(a,b))