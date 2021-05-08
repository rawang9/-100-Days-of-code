from turtle import Turtle
import random
COLOR=['red','green','yellow','blue','orange']
MOVE_DIST=5


class Car():
    def __init__(self):
        self.carbox=[]
    def createcar(self):
        turn=random.randint(1,6)
        if turn==1:
            hero=Turtle('square')
            hero.shapesize(stretch_wid=1,stretch_len=2)
            hero.penup()
            hero.color(random.choice(COLOR))
            hero.setheading(180)
            hero.goto(300,random.randint(-250,250))
            self.carbox.append(hero)

    def move(self):
        for cars in self.carbox:
            cars.forward(MOVE_DIST)


