from turtle import Turtle,Screen,colormode
import random
t1 = Turtle()

colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

angle = [0,90,180,270,360]
t1.shape("turtle")
t1.speed("fastest")
forwordamount = 100
angleamount = 90

#t1.dot(100,random_color())#First number is the size of the dot and the second number is the rgb color which we can just use  random color choice method since it returns a rgb color

#t1.goto(300,0)#Changes the position of the turtle which is 0,0 initially

t1.hideturtle()#Hides the turtle
t1.penup()#To hide the pencil writings between locations
for i in range(100):
    t1.dot(random.randint(10,50),random_color())
    t1.goto(random.randint(-300,300),random.randint(-300,300))

screen = Screen()
screen.exitonclick()