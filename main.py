from colorgram import extract
from turtle import Turtle, Screen
import random


def extract_colors():
    colors = extract('image.jpg', 30)
    rgb = []
    for c in colors:
        r = c.rgb.r
        g = c.rgb.g
        b = c.rgb.b
        new_color = (r, g, b)
        rgb.append(new_color)
    return rgb


def create_painting():
    timmy = Turtle()
    timmy.penup()
    timmy.speed("fastest")
    timmy.hideturtle()
    screen = Screen()
    screen.colormode(255)
    colors = extract_colors()
    y_pos = -250
    for _ in range(10):
        timmy.setposition(-250, y_pos)
        for i in range(10):
            timmy.dot(20, random.choice(colors))
            timmy.forward(50)
        y_pos += 50
    screen.exitonclick()


create_painting()
