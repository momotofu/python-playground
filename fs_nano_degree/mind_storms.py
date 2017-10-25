#Class practice
import turtle

def draw_square(shift):
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)
    brad.right(shift)

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

def draw_triangle(shift):
    chris = turtle.Turtle()
    chris.shape("turtle")
    chris.color("purple")
    chris.right(shift)

    for i in range(0, 3):
        chris.right(120)
        chris.forward(100)

window = open_window()
# draw_circle()
for i in range(36):
    draw_square(i * 10)
# draw_triangle()

window.exitonclick()

