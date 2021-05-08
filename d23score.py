from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.hideturtle()
        self.up()
        self.goto(-260,250)
        self.levelup()

    def levelup(self):
        self.clear()
        self.write(f"Level : {self.level}",False,align='left',font=("Arial", 20, "normal"))
        self.level+=1
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over!",False,align='center',font=("Arial", 40, "normal"))
