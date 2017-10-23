#Class practice

import turtle


def draw_square():

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)

    for i in range(0, 100):
        brad.right(30)
        brad.forward(16)
        for i in range(0,4):
            brad.forward(100)
            brad.right(90)

def open_window():
    window = turtle.Screen()
    window.bgcolor("yellow")
    window.exitonclick()

open_window()
draw_square()


