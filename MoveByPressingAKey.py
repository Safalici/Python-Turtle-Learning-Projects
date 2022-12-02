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
screen = Screen()


def moveRight():
    t1.forward(10)
def moveLeft():
    t1.left(90)
screen.listen()
screen.onkey(key= "space", fun=moveRight )

screen.onkey(key= "l", fun=moveLeft )

screen.exitonclick()