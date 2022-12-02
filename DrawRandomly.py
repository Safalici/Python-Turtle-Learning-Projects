from turtle import Turtle,Screen
import random
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()

angle = [0,90,180,270,360]
t1.shape("turtle")
t1.color("blue")
forwordamount = 20
t2.speed("fastest")
t2.color("red")
t2.shape("turtle")

t3.speed("fastest")
t3.color("black")
t3.shape("turtle")

t4.speed("fastest")
t4.color("purple")
t4.shape("turtle")

for i in range(400):
    t1.forward(forwordamount)
    t1.right(random.choice(angle))
    t2.forward(forwordamount)
    t2.right(random.choice(angle))
    t3.forward(forwordamount)
    t3.right(random.choice(angle))
    t4.forward(forwordamount)
    t4.right(random.choice(angle))



screen = Screen()
screen.exitonclick()