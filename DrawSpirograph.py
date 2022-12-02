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

def draw(angle):
    for i in range(int(360/angle)):
        t1.color(random_color())
        #t1.circle(100) #raidus of the circule '100'
        t1.forward(forwordamount)
        t1.right(angleamount)
        t1.forward(forwordamount)
        t1.right(angleamount)
        t1.forward(forwordamount)
        t1.right(angleamount)
        t1.forward(forwordamount)
        t1.right(angleamount)
        
        t1.setheading(t1.heading()+angle)
    

draw(5)



screen = Screen()
screen.exitonclick()