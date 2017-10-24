def open_window():
    window = turtle.Screen()
    window.bgcolor("pink")
    return window

def draw_tree(number_of_branches, amount):
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
        mi.shape("turtle")
        mi.color("green")
        mi.speed(2)

        zu = turtle.Turtle()
        zu.shape("turtle")
        zu.color("green")
        zu.speed(2)

        # draw a line
        mi.forward(amount)
        zu.setpos(mi.pos())


window.exitonclick()
