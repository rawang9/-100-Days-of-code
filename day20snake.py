from turtle import Turtle
MOVE_DIST=20#use captial later to define constant
TURN=90
UP,DOWN,LEFT,RIGHT=90,270,180,0
class Snake:
    def __init__(self):
        self.tur=[]
        self.create_snake(0)
        self.head=self.tur[0]
        self.tail=self.tur[-1]
    def create_snake(self,xasis):
        for i in range(3):
            snake=Turtle("square")
            #snake.shapesize(0.5,0.5)
            snake.color('white')
            snake.up()
            xasis-=20
            snake.goto(xasis,0)
            self.tur.append(snake)
            
    def move(self):
        for seg_num in range(len(self.tur)-1,0,-1):

            self.tur[seg_num].goto(self.tur[seg_num-1].position())
        self.tur[0].forward(MOVE_DIST)
    def ifeat(self):
        snake=Turtle("square")
        snake.color('white')
        snake.up()
        
        snake.goto(self.tur[-1].position())
        self.tur.append(snake)

        
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
        
        
        
                                
