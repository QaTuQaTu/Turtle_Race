from turtle import*
from random import randint
from time import sleep


finish=200
def startRace(t,x,y,color):
    t.color(color)
    t.shape('turtle')
    t.speed(100)
    t.penup()
    t.goto(x,y)
def dance(t): 
    t.speed(15)
    t.left(randint(0, 90))
    j = 0
    while j < 8:
        t.penup()
        t.goto(0, 0)
        t.pendown()
        i = 1
        while i < 32:
            t.forward(i)
            t.left(1/2+5)
            i += 1
        j += 1
    t.penup()
    t.goto(0, 0)
t1=Turtle()
t2=Turtle()
t3=Turtle()
startRace(t1, -200, -20, "red") 
startRace (t2, -200, 20, 'blue')
startRace (t3, -200, 3, 'green')
sleep(1)
while t1.xcor() < finish and t2.xcor() < finish and t3.xcor() < finish:
    t1. forward (randint(2,7))
    t2. forward (randint(2,7))
    t3. forward (randint(2,7))
sleep(1)
# calculating totals:
t1.clear()
t2.clear()
t3.clear()
max_x = max(t1.xcor(), t2.xcor(), t3.xcor())
if t1.xcor() == max_x:
    dance(t1)
    sleep(1)
# calculating totals:
    t1.clear()
    t2.clear()
    t3.clear()
    max_x = max(t1.xcor(), t2.xcor(), t3.xcor())
    if t1.xcor() == max_x:
        dance(t1)
    if t2.xcor() == max_x:
        dance(t2)
    if t3.xcor() == max_x:
        dance(t3)

