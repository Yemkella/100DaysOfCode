import turtle
import random
screen = turtle.Screen()
turtle.colormode(255)
tim = turtle.Turtle()
tim.width(1)
tim.speed("fastest")

def random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    color = (red,green,blue)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
    
def draw_shape(edges):
    angle = 360 / edges
    for n in range(edges):
        tim.forward(100)
        tim.right(angle)


def random_walk(lines,colors):
    direction = ["right", "left"]
    for n in range(lines):
        tim.speed("fastest")
        tim.color(random_color())
        tim.forward(25)
        direction_choice = random.choice(direction)
        if direction_choice == "right":
            tim.right(90)
        else:
            tim.left(90)

# for edges in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(edges)

# random_walk(600,colors)

screen.exitonclick()