import turtle
import random

def create_shape(shape, color):
    t = turtle.Turtle()
    t.shape(shape)
    t.color(color)
    t.penup()
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    t.goto(x, y)
    return t

def check_collision(t1, t2):
    distance = t1.distance(t2)
    if distance < 20:  
        return True
    return False


wn = turtle.Screen()
wn.tracer(0)


player = turtle.Turtle()
player.shape("turtle")  
player.color("blue")
player.penup()
player.goto(0, -250)


num_shapes = 5
shapes = []
possible_shapes = ["square", "circle", "arrow", "classic"]
colors = ["red", "green", "orange", "purple", "yellow", "black", "pink", "blue"]
for _ in range(num_shapes):
    shape = random.choice(possible_shapes)
    color = random.choice(colors)
    t = create_shape(shape, color)
    shapes.append(t)


dy = 0
gravity = 0.05  
speed_increase = 0.005  

score = 0


def move_left():
    x = player.xcor()
    x -= 10
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 10
    player.setx(x)

def move_up():
    y = player.ycor()
    y += 10
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= 10
    player.sety(y)


wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")


while True:
    wn.update()

    
    dy -= gravity
    y = player.ycor() + dy
    if y < -250:  
        y = -250
        dy *= -0.8  
    player.sety(y)

    
    for shape in shapes:
        if check_collision(player, shape):
            shape.hideturtle()
            shapes.remove(shape)
            
            if shape.shape() == "square":
                score += 10
            elif shape.shape() == "circle":
                score += 20
            elif shape.shape() == "arrow":
                score += 30
            
            new_shape = random.choice(possible_shapes)
            new_color = random.choice(colors)
            new_t = create_shape(new_shape, new_color)
            shapes.append(new_t)
            gravity += speed_increase  

    
    for shape in shapes:
        dy -= gravity
        y = shape.ycor() + dy
        if y < -250:  
            y = -250
            dy *= -0.8  
        shape.sety(y)

    
    wn.title("Score: {}".format(score))
