import turtle
t = turtle.Turtle()
def rect():
    for i in range(2):
        t.forward(400)
        t.right(90)
        t.forward(250)
        t.right(90)
turtle.bgcolor('grey')
turtle.setup(500,500)
t.penup()
t.goto(-200,125)
t.pendown()
t.color('white')
t.begin_fill()
rect()
t.end_fill()
t.penup()
t.goto(0,-77.5)
t.pendown()
t.color('red')
t.begin_fill()
t.circle(75)
t.end_fill()





turtle.done()
turtle.exitonclick()