import turtle

def open_window():
    window = turtle.Screen()
    window.bgcolor("pink")
    return window

def draw_tree(number_of_branches, amount, a_pos, b_pos, a_deg, b_deg):
    newAmount = amount * 0.9
    """
    draw a line
    then split into two
    draw a line with a shorter distance
    then split into two
    """
    if number_of_branches <= 0:
        return
    else:
        mi = turtle.Turtle()
        mi.penup()
        mi.color("green")
        mi.speed(10)
        mi.setpos(a_pos)
        mi.shapesize(0.5)
        mi.setheading(a_deg)

        zu = turtle.Turtle()
        zu.penup()
        zu.color("green")
        zu.speed(10)
        zu.shapesize(0.5)
        zu.setpos(b_pos)
        zu.setheading(b_deg)

        # draw a line
        mi.pendown()
        zu.pendown()
        mi.forward(newAmount)
        zu.setpos(mi.pos())
        # split
        mi.right(15)
        zu.left(15)
        mi.forward(newAmount * 0.95)
        zu.forward(newAmount * 0.95)

        return draw_tree(number_of_branches - 1, amount * 0.95, mi.pos(), zu.pos(), mi.heading(), zu.heading())

window = open_window()
draw_tree(20, 30, (0,0),(0, 0), 0, 0)
window.exitonclick()
