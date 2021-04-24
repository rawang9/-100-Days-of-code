# =============================================================================
# import turtle
# 
# timmy= turtle.Turtle()
# timmy.color('red')
# timmy.shape('turtle')
# timmy .forward(100)
# 
# screen=turtle.Screen()
# print(screen.canvheight )
# screen.exitonclick()
# =============================================================================
# from prettytable import PrettyTable
# table=PrettyTable()
# table.add_column("Pokemon Name",["Picachu","Squirtle","Chamander"])
# 
# table.add_column("Type",["Electric","Water","Fire"])
# table.align= 'l'
# print(table)
# =============================================================================

from day16_menu import Menu, MenuItem
from day16_coffee_maker import CoffeeMaker
from day16_money_machine import MoneyMachine
menu=Menu()
money=MoneyMachine()
maker=CoffeeMaker()
is_on=True

while is_on:
    ask=input(f"What would you like? {menu.get_items()}: ")
    if ask=='off':
        is_on=False
    elif ask=='report':
        maker.report()
        money.report()
    else:
        drink=menu.find_drink(ask)
        if maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
             maker.make_coffee(drink)