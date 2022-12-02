from turtle import Turtle,Screen,colormode
import random


colormode(255)
screen = Screen()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

angle = [0,90,180,270,360]


screen.setup(700,700)#First parameter is width second one is high

#result = screen.textinput(title= "Calculate", prompt="5*4=?")
#print(result)

turtles = []
y = -200
for i in range(10):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(random_color())
    new_turtle.speed("fastest")
    new_turtle.goto(-280,y)
   
    turtles.append(new_turtle)
    y+=50
    
finish = False
while True:
    for turtle in turtles:
        turtle.speed("fastest")
        turtle.forward(random.randint(1,10))
        if turtle.xcor()>250:
            turtle.write("I WON!", font=("Arial", 15, "bold"))
            finish = True
            break
    if finish:
        break       





screen.exitonclick()