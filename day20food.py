from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)      
        self.color("green")        
        self.speed('fastest')
        self.refres()
        
    def refres(self):
        xaxs=random.randint(-280,280)
        yaxs=random.randint(-280,280)
        self.goto(xaxs,yaxs)