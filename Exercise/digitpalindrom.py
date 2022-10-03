def is_palindrom(number):
  a = str(number)
  if a == a[::-1]:
    return True
  else:
    return False
a = "1"
b = "10"
carpim = 0
first = 0
second = 0
digit = int(input("How many digit do you want? : "))
for i in range(1,digit):
  a += "0"
  b += "0"
for i in range(int(a),int(b)):
  for j in range(int(a),int(b)):
    times = j*i
    if is_palindrom(times) and carpim < times:
      carpim = times
      first = i
      second = j
  
print(first,second,carpim)     
