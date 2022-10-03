from coffee import name
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 0
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 500,
    "milk": 500,
    "coffee": 500
}

case = {
    "money" : 0
}

password = 1453

def customer_menu():
    while True:                    
        print(name)
        order = input("What would you like? (espresso/latte/cappucino): ").lower()                
        if order.isalpha():                                
            if order == "off":
                    print("The system has been quited from Machine")
                    break
            elif order == "latte" or order == "espresso" or order == "cappuccino":
                if check_resources(order):                                        
                        show_report(order)
                        check_resources(order)
                        processing(order)  
                else:
                    for i in resources:
                            if resources[i] < MENU[order]["ingredients"][i]:
                                print(f"Sorry there is not enough {i}")
            else:
                print(f"You made a mistake for choosing. Please try again!")
        else:
            print(f"Please write as alpabetic. You only choose Latte, espresso or cappuccino!")
            
def check_resources(var):    
    for i in resources:    
        if resources[i] < MENU[var]["ingredients"][i]:
            return False
    return True    

def adding_resource():
    for i in resources:
        print(f"{i.capitalize()}: {resources[i]}")                
    res = input("1-Water 2-Milk 3-Coffee\nWhich resource do you want?: ")
    if res == "1":
        ml = int(input("How much mililiter water do you add?:"))
        resources["water"] += ml
        print("Adding process is succesful.")
    elif res == "2":
        ml = int(input("How much milileter milk do you add?:"))
        resources["milk"] += ml
        print("Adding process is succesful.")                                
    elif res == "3":
        g = int(input("How much gram coffe do you add?:"))
        resources["coffee"] += g
        print("Adding process is succesful.")
    else:
        print("There may not enough in case that you entered! Try again!")

def check_money(var):
    if check_resources(var):
        quarter = int(input("How many quarter to insert: "))
        dimes = int(input("How many dimes to insert: "))
        nickels = int(input("How many nickles to insert: "))
        pennies = int(input("How many pennies to insert: "))
        total = (quarter*0.25)+(dimes*0.1)+(nickels*0.05)+(pennies*0.01)
        if total > MENU[var]["cost"]:
            change = "{:.2}".format(total-MENU[var]["cost"])
            
            print("Here is",change,"dollars in change.","\n","Your coffe is preparing, please wait")
            return True  
        
        elif total == MENU[var]["cost"]:
            print("Your coffe is preparing, please wait")
            return True    
        
        else:    
            print("Sorry that's not enough money. Money refunded.")
            return False
       
def show_report(var):
    for i in MENU[var]:
        if i == "cost":            
            print("Cost:",MENU[var][i],"$")
            break
        for j in MENU[var][i]:
            print(f"{j.capitalize()}: {MENU[var][i][j]}")
        
def processing(order):
    if check_money(order):
        for i in resources:
            for j in MENU[order]:
                if j == "cost":
                    break
                else:
                    resources[i] -= MENU[order][j][i]
        case["money"] += MENU[order]["cost"]

def withdrawmoney():
    while True:
        wmoney = float(input("Press 0(zero) to quit.\nHow much money do you withdraw?: "))
        if wmoney > case["money"]:
            print(f"The case doesn't have this amount.The current amount is",case["money"])
        else:            
            case["money"] -= wmoney
            break

def reportfor_staff():
    for i in resources:
        print(f"{i.capitalize()}: {resources[i]}")
    print("Money:",case["money"])

def staff_menu():
    counter = 3 # Kullanıcının kalan hakkı
    while counter > 0:
        try:        
            password_query = int(input("Please enter password of the system: "))
            if password_query == password:
                print("Welcome to the system of the machine.")
                cont = True
                while cont:
                    print("Main Menu:\n1-Adding Resource\n2-Withdraw Money\n3-Report of System\n0-Quit")
                    main_option = input("What do you want to do?: ").lower()
                    if main_option == "3":
                        reportfor_staff()
                        opt = input("1-Menu\n0-Back: ")
                        if opt == 0:
                            cont = False
                            
                        
                    elif main_option == "1":
                        adding_resource()
                                                
                    elif main_option == "2":
                            withdrawmoney()
                                                    
                    elif main_option == "0":
                        cont = False
                        counter = 0
                    else:
                        print("Mistaken enter! Try again!")
            else:
                print("You enterd wrong password. Try again.")
                print(f"You left {counter-1} rights.")
                counter -= 1
        except:
            print("Invalid enter! Try again!")
        
while True:
    user_query = input("Are you staff or customer? (staff/customer): ").lower()
    
    if user_query.isalpha():
        if user_query == "staff":
            staff_menu()
                   
        elif user_query == "customer":
            customer_menu()

        else:
            print("You only have two choices: Staff or Customer !")
    else:
        print("Invalid enter! Please write as alphabetic!")