from turtle import Turtle,Screen
t = Turtle()

t.shape("turtle")
t.color("blue")
forwordamount = 5

for j in range(4):
    t.left(90)
    #this for loop goes 100 pages
    for i in range(10):
        t.pendown()
        t.pencolor("red")
        t.forward(forwordamount)
        t.penup()
        t.forward(forwordamount)
        t.pendown()
        t.pencolor("blue")
        t.forward(forwordamount)
        t.penup()
        t.forward(forwordamount)
    
    










screen = Screen()
screen.exitonclick()