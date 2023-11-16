# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
import turtle
import random

colors = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


screen = turtle.Screen()
turtle.colormode(255)
painter = turtle.Turtle()
painter.width(20)
painter.speed("normal")
painter.shape("circle")


def random_color(colors):
    color = random.choice(colors)
    return color


def paint(painter, colors):
    painter.color(random_color(colors))
    painter.dot(20)


y = -250
for _ in range(10):
    x = -250
    for _ in range(10):
        painter.teleport(x, y)
        paint(painter, colors)
        x += 50
    y += 50


screen.exitonclick()
