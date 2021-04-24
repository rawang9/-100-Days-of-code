#coffy machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resource={'water':300,'milk':200,'coffee':100,'Money':0}

def add_money():
    '''
    the the diffrent coin and return the total values
    of all the coin
    '''
    money={'quarters':0.01,'dimes':0.10,'nickel':0.05,'pennies':0.25}
    total=0
    for key in money:
        total+=money[key]*int(input(f"how namy {key}? : "))
    return total

def dispreport():
    '''check the stock'''
    for key in resource:
        if key=='coffee':
            print(f"{key} : {resource[key]}g")
        elif key=='Money':
            print(f"{key} : ${resource[key]}")
        else:
            print(f"{key} : {resource[key]}ml")            
def maker(flavour):
    '''
    check the stock for making the coffee
    '''
    for key in MENU[flavour]["ingredients"]:
        if resource[key]<MENU[flavour]["ingredients"][key]:
            print(f"Sorry there is not enough {key}")
            return flag==False
    for key in MENU[flavour]["ingredients"]:
        resource[key]-=MENU[flavour]["ingredients"][key]
    return True
            

while True:        
    ask=input("What would you like? (espresso/latte/cappuccino): ")
    flag=True
    if ask=='report':
        dispreport()
    elif ask in list(MENU.keys()):
        flag=maker(ask)
        if flag:
            print("Please insert coins.")
            print()
            change="{:.2f}".format(add_money() - MENU[ask]['cost'])
            
            if float(change)>0:
                print(f"Here is ${change} in change.")
                resource['Money']+=MENU[ask]['cost']
                maker(ask)
                print(f"Here is your {ask} :-) Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded !")
        else:
            continue
    else:
        break
