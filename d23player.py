from turtle import Turtle
MOVE_DIST=50

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')

        self.up()
        self.setheading(90)
        self.goto(0,-280)
    def move(self):
        self.forward(MOVE_DIST)