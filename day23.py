from turtle import Screen
from d23player import Player
from d23score import Score
from d23car import Car
import time
screen=Screen()
screen.bgcolor('white')
screen.setup(600,600)
screen.tracer(0)
screen.title("")


#scoreboad
score=Score()

#cars
car=Car()
#player
player=Player()
screen.listen()
screen.onkey(player.move,'Up')
def Game():

    game_on=True
    speed=0.09
    while game_on:
        time.sleep(speed)
        screen.update()
        car.createcar()
        car.move()
        for hit in car.carbox:
            if player.distance(hit)<20:
                score.gameover()
                game_on=False
        if player.ycor()>250:
            player.goto(0,-280)
            speed-=0.01
            score.levelup()

Game()

screen.exitonclick()