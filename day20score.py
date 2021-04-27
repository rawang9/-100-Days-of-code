from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-30,280)
        self.start=-1
        
    def scoreup(self):
        self.start+=1   
        self.clear()
        self.write(f"Your Score is : {self.start}",False,align='center', font=("Arial", 15, "normal"))
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over !",False,align='center', font=("Arial", 15, "normal"))
    