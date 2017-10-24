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
        mi.speed(20)
        mi.setpos(a_pos)
        mi.shapesize(0.5)
        mi.setheading(a_deg)

        zu = turtle.Turtle()
        zu.penup()
        zu.color("green")
        zu.speed(20)
        zu.shapesize(0.5)
        zu.setpos(b_pos)
        zu.setheading(b_deg)

        # draw a line
        mi.pendown()
        zu.pendown()
        mi.forward(newAmount)
        zu.setpos(mi.pos())
        # split
        mi.right(35)
        zu.left(30)
        mi.forward(newAmount * 0.97)
        zu.forward(newAmount * 0.97)

        draw_tree(number_of_branches - 1, amount * 1.06, mi.pos(), zu.pos(), mi.heading(), zu.heading())
        draw_tree(number_of_branches - 1, amount * 1.06, mi.pos().x - 1, zu.pos().x - 1, mi.heading(), zu.heading())

window = open_window()
draw_tree(200, 1, (0,0),(0, 0), 0, 0)
window.exitonclick()
