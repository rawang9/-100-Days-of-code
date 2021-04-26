# =============================================================================
# import turtle
# tom=turtle.Turtle()
# tom.forward(100)
# for i in range(3):
#     tom.right(90)
#     tom.forward(100)
# turtle.exitonclick()
# 
# =============================================================================
# =============================================================================
# import turtle as tt
# tom=tt.Turtle()
# for i in range(50):
#     tom.forward(4)
#     tom.penup()
#     tom.forward(4)
#     tom.pendown()
# tt.exitonclick()
# 
# =============================================================================
# =============================================================================
# import turtle as tt
# import random
# tom=tt.Turtle()
# color=["black", "red","green"]
# for i in range(3,10):
#     angel=360/i
#     tom.color(random.choice(color))
#     for j in range(i):
#         tom.right(angel)
#         tom.forward(100)
# tt.exitonclick()
# 
# =============================================================================
# =============================================================================
# import turtle as tt
# import random
# tt.colormode(255)
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     return (r,g,b)
# tom=tt.Turtle()
# color=["red","green","CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
# direction=[0,90,180,270]
# for i in range(200):
#     tom.color(random_color())
#     tom.forward(30)
#     tom.setheading(random.choice(direction))
#     tom.speed(50)
#     tom.pensize(0.1*i)
# tt.exitonclick()
# 
# =============================================================================
# =============================================================================
# import turtle as tt
# import random
# tt.colormode(255)
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     return (r,g,b)
# tom=tt.Turtle()
# tom.speed('fastest')
# color=["red","green","CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
# def draw_spiinograph(size_of_gap):
#     for i in range(360//size_of_gap):
#         tom.color(random_color())
#         tom.circle(100)
#         tom.setheading(tom.heading()+size_of_gap)
# draw_spiinograph(10)
# tt.exitonclick()
# =============================================================================

# the color generator from image=============================================================================
# import colorgram
# colorbox=[]
# color=colorgram.extract('spot.jpg', 32)
# for frst in color:
#     
#     r,g,b=frst.rgb.r,frst.rgb.g,frst.rgb.b
#     tup=(r,g,b)
#     colorbox.append(tup)
# print(colorbox)
# 
# =============================================================================
import turtle as tt
import random
tt.colormode(255)
color_lis=[ (198, 166, 109), (141, 77, 54), (73, 98, 123), (158, 148, 54),  (213, 203, 144),(120, 39, 29), (137, 160, 179), (70, 108, 74), (144, 176, 139), (195, 91, 70), (69, 52, 46), (96, 81, 89), (60, 52, 56), (224, 177, 163), (102, 141, 131), (97, 130, 164), (156, 141, 159), (49, 60, 83), (73, 67, 50), (111, 38, 42), (47, 56, 72), (108, 136, 140), (182, 199, 183), (182, 190, 205), (168, 101, 106), (51, 76, 61), (213, 181, 184), (180, 195, 199)]
tom=tt.Turtle()
tom.hideturtle()
tom.penup()
tom.setheading(225)
tom.forward(300)
tom.setheading(0)
tom.speed('fastest')
no_of_dot=100
for i in range(1,no_of_dot+1):
    tom.dot(20,random.choice(color_lis)) 
    tom.forward(50)
    if i%10==0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)
screen=tt.Screen()
screen.exitonclick()