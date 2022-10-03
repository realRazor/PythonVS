# Is prime number which you enter?

while True:
    try:
        number = int(input("Please enter any number: "))
        count = 0
        for i in range(2,number):
            if number % i != 0:
                count = count
            else:
                count += 1 
        if count == 0:
            print(f"{number} is a prime number.")       
        else:
            print(f"{number} is not a prime number.") 
    except:
        print("Invalid entry! Please write as numeric")
