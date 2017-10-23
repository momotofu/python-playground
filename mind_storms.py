#Class practice
import turtle

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)

    for i in range(0,4):
        brad.forward(100)
        brad.right(90)

def open_window():
    window = turtle.Screen()
    window.bgcolor("pink")
    return window

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.shapesize(3)
    angie.tilt(2)
    angie.color('red')

    angie.circle(100)

def draw_triangle():
    chris = turtle.Turtle()
    chris.shape("turtle")
    chris.color("purple")

    for i in range(0, 3):
        chris.right(120)
        chris.forward(100)

window = open_window()
draw_circle()
draw_square()
draw_triangle()

window.exitonclick()

