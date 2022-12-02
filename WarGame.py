from turtle import Turtle,Screen,colormode
import random
import time
screen = Screen()
screen.setup(700,700)#First parameter is width second one is high
our_life = 100
enemy_life = 100

we = Turtle()

enemy = Turtle()
we.penup()
enemy.penup()

we.shape("turtle")
enemy.shape("turtle")
we.color("blue")
enemy.color("red")

we.goto(-200,0)
enemy.goto(200,0)
enemy.setheading(180)

we.write(f"{our_life}", font=("Arial",20,"normal"))
enemy.write(f"{enemy_life}", font=("Arial",20,"normal"))

def attack():
    global enemy_life
    global our_life
    we.goto(200,0)
    
    enemy_life -= random.randint(10,30)
    enemy.clear()
    if enemy_life < 0:
        enemy_life = 0
    enemy.write(f"{enemy_life}", font=("Arial",20,"normal"))
    we.goto(-200,0)
   # time.sleep(1)
    enemy.goto(-200,0)

    our_life -= random.randint(20,30)
    we.clear()
    if our_life < 0:
        our_life = 0
    we.write(f"{our_life}", font=("Arial",20,"normal"))
    enemy.goto(200,0)
    if our_life <= 0:
            
            we.clear()
            we.write("We lost :(", font=("Arial",20,"normal"))
    if enemy_life <= 0:
            we.clear()
            we.write("We won :)", font=("Arial",20,"normal"))


screen.listen()
screen.onkey(key="space",fun=attack)


screen.exitonclick()