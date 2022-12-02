from turtle import Turtle,Screen,colormode
import random
t1 = Turtle()

colormode(255)
screen = Screen()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

angle = [0,90,180,270,360]
t1.shape("turtle")
t1.speed("fastest")

screen.setup(1000,600)#First parameter is width second one is high

result = screen.textinput(title= "Calculate", prompt="5*4=?")
print(result)



screen.exitonclick()