from turtle import Turtle
import random
MID_LINE=25
MOVE_DIST=20#use captial later to define constant
UP,DOWN=90,270
class WhiteDot(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor('white')
        self.pensize(8)
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.goto(0,-790)
        self.setheading(90)
        self.p1score=0
        self.p2score=0
        for i in range(25):
            self.pendown()
            self.forward(MID_LINE)
            self.penup()
            self.forward(MID_LINE)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-30,350)
        self.pendown()
        self.p1score=0
        self.p2score=0
        self.scorepri()
    def scorepri(self):
        self.clear()
        self.write(f" P1:{self.p1score}   P2:{self.p2score} ",False,align='center', font=("Arial", 45, "normal"))
    def scorep1(self):
        self.p1score+=1
        self.scorepri()
    def scorep2(self):
        self.p2score+=1
        self.scorepri()
    def result(self):
        self.penup()
        self.goto(-160,150)
        if self.p1score>self.p2score:
            self.write(f"Player:1 won the game  by {self.p1score} Point",False,align='center', font=("Arial", 40, "normal"))
        elif self.p1score==self.p2score:
            self.write("  Game-Draw ",False,align='center', font=("Arial", 40, "normal"))

        else:
            self.write(f"Player:2 won the game  by {self.p2score} Points",False,align='center', font=("Arial", 40, "normal"))

class Board(Turtle):
    def __init__(self,brd):
        super().__init__()
        self.tom=[]

        self.brdp=brd
        self.axis=0
        self.create()
        self.head=self.tom[0]
        self.head.goto(self.brdp)
        self.head.setheading(UP)



    def create(self):
        for i in range(6):
            tim=Turtle('square')
            tim.color('white')
            tim.up()
            tim.goto(self.brdp)
            self.tom.append(tim)

    def move(self):
        for pow in range(len(self.tom)-1,0,-1):
            pos=self.tom[pow-1].position()
            self.tom[pow].goto(pos)
        self.head.forward(MOVE_DIST)


    def up(self):
        self.head.setheading(UP)
    def down(self):
       self.head.setheading(DOWN)

    def wallcolis(self):
        if  self.head.ycor()>380:
            self.down()
        elif self.head.ycor()<-380:
            self.up()
DIRECTION=[30,15,0,345,330]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('red')

        self.dir=random.randint(330,390)
        self.setheading(self.dir)
        self.goto(-100,0)
    def ballmv(self):
        self.forward(20)
        if self.ycor()>380 or self.ycor()<-380:
            self.setheading(360-self.dir)
            self.dir=360-self.dir


