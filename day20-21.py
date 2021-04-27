from turtle import Screen
import time
from day20snake import Snake
from day20food import Food
from day20score import Score
screen=Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)
screen.title("The snake Game")
screen.tracer(0)


score=Score()
score.scoreup()
snake = Snake()
food=Food()
screen.listen()
#kwyboard play
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
#flag
game_on=True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #if eat a frog
    if snake.head.distance(food)<15:
            food.refres()
            score.scoreup()
            snake.ifeat()
    #if hit a wall
    if snake.head.xcor()>290 or snake.head.ycor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290:
        score.gameover()
        game_on=False
    #if hit its own body
    for segment in snake.tur[1:]:
        if snake.head.distance(segment)<10:
            score.gameover()
            game_on=False
screen.exitonclick() 