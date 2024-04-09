import turtle,time

wn = turtle.Screen()
wn.tracer(0)

turtle.speed(0)
turtle.shape("square")
turtle.penup()

dy = 0
gravity = 0.1

while True:
    wn.update()
    dy -= gravity
    turtle.sety(turtle.ycor() + dy)

    if turtle.ycor() < -300:
        dy -= gravity *2
        dy *= -1