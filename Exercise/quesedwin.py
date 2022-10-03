
def plus(x,y):
    return (lambda x,y : x+y)(x,y)

def minus(x,y):
    return (lambda x,y : x-y)(x,y)
    
def multiply(x,y):
    return (lambda x,y : x*y)(x,y)
    
def divided(x,y):
    return (lambda x,y : int(x/y))(x,y) 

while True: 
    first = int(input("İlk sayınız: "))
    
    symbol = input("İşleminiz: ")
    
    second = int(input("ikini sayınız: "))
    

    calc = {
        "+" : plus(first,second),
        "-" : minus(first,second),
        "*" : multiply(first,second),
        "/" : divided(first,second)
    }

    for i in calc.keys():
        if i == symbol:
            print(calc[i])