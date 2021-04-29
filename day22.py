from turtle import Screen
import time
from day22tur import WhiteDot,Score,Board,Ball
screen=Screen()
screen.setup(width=1200,height=800)
screen.title("The PONG GAME :-) ")
screen.bgcolor('Black')
screen.tracer(0)

whit=WhiteDot()

score=Score()

ball=Ball()
board1=Board((580,0))
board2=Board((-580,0))

screen.listen()
screen.onkey(board1.up,"Up")
screen.onkey(board1.down,"Down")
screen.onkey(board2.up,"w")
screen.onkey(board2.down,"s")

def Game():
    rflag=False
    lflag=False
    game_flag=True
    while game_flag:
        rflag=False
        lflag=False
        screen.update()
        time.sleep(0.05)
        board1.move()
        board2.move()
        board1.wallcolis()
        board2.wallcolis()
        ball.ballmv()
        for i in range(len(board1.tom)):
            if board1.tom[i].distance(ball)<15:
                ball.setheading(ball.dir-180)
                ball.dir=ball.dir-180
                score.scorep2()
                rflag=True
                break
        for i in range(len(board1.tom)):
            if board2.tom[i].distance(ball)<15:
                ball.setheading(ball.dir-180)
                ball.dir=ball.dir-180
                score.scorep1()
                lflag=True
                break
        if (ball.xcor()>580 and rflag==False) or (ball.xcor()<-580 and lflag==False):
            score.result()
            game_flag=False

Game()

screen.exitonclick()