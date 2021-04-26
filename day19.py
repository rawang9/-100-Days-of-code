# =============================================================================
# #the drawing board
# import turtle as dd
# tim=dd.Turtle()
# screen=dd.Screen()
# 
# def move():
#     tim.forward(10)
# def movebck():
#     tim.backward(10)
# def antic():
#     tim.left(10)
# def clock():
#     tim.right(10)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
# screen.listen()
# screen.onkey(fun=move,key="w")
# screen.onkey(fun=movebck,key="s")
# screen.onkey(fun=antic,key="a")
# screen.onkey(fun=clock,key="d")
# screen.onkey(clear,'c')
# screen.exitonclick()
# 
# 
# 
# =============================================================================
from turtle import Turtle,Screen
import  random
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Put you bet: ",prompt="chose the turtle")
turs=[]
pos=170
player="t1"
color=["red","orange","yellow","green","blue","purple"]
def fun(name,n,pos):
    
    name=Turtle(shape="turtle")
    name.color(color[n])
    name.penup()
    name.goto(-230,pos)
    turs.append(name)

for i in range(len(color)):
    newy=-1*pos
    fun(player+str(i),i,-1*pos)
    pos-=65
flag=False
if user_bet:
    flag=True
while flag:
    for tur in turs:
        if tur.xcor()>230:
            flag=False
            wining_tur=tur.pencolor()
            if wining_tur==user_bet:
                print(f"You won ! {wining_tur} won the game")
            else:
                print(f"you lost !      {wining_tur} won the game")
        tur.forward(random.randint(5,10))
screen.exitonclick()