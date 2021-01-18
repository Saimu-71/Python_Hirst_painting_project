import turtle as t
import random
ball=t.Turtle()
t.colormode(255)
#ball.speed("fastest")
"""import colorgram #pip install colorgram.py  typing in terminal
colors=colorgram.extract("img.jpg",30)
color_rgb=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new=(r,g,b)
    color_rgb.append(new)


print(color_rgb) #print the color then copy the rgb color value"""
color_list=[(210, 154, 95), (189, 60, 29), (225, 212, 111), (234, 215, 224), (209, 147, 178), (177, 157, 44), (222, 225, 237), (224, 233, 226), (92, 103, 187), (28, 26, 69), (79, 84, 147), (37, 40, 19), (196, 20, 7), (29, 45, 28), (225, 168, 197), (146, 151, 188), (208, 90, 63), (43, 44, 104), (232, 174, 162), (146, 66, 80), (190, 13, 19), (181, 182, 217), (207, 81, 107), (84, 97, 85), (154, 165, 155), (44, 26, 45), (69, 70, 44), (222, 206, 26), (52, 71, 55)]
ball.setheading(225)
ball.penup()
ball.hideturtle()
ball.forward(325)
ball.setheading(0)
number=100
for i in range(1,number+1):
    ball.dot(20,random.choice(color_list))
    ball.forward(50)
    if i%10==0:
        ball.setheading(90)
        ball.forward(50)

        ball.setheading(180)
        ball.forward(500)

        ball.setheading(0)







screen=t.Screen()
screen.exitonclick()