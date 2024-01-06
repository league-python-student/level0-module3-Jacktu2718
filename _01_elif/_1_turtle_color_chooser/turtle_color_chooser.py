import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    jack = turtle.Turtle()
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    for i in range(4):
        jack.forward(350)
        jack.right(90)

    #      3) Set the pen width to 10
    jack.pensize(30)
    #      4) Ask the user what color pen they would like to draw with
    color = simpledialog.askstring(title='what color?', prompt='what color would you like to draw with?')
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    if color == "blue":
        jack.pencolor("blue")
    elif color == "red":
        jack.pencolor("red")
    elif color == "purple":
        jack.pencolor("purple")
    elif color == "yellow":
        jack.pencolor("yellow")
    elif color == "green":
        jack.pencolor("green")
    elif color == "orange":
        jack.pencolor("orange")
    #      6) If the user doesn't enter anything, choose a random color
    elif color == "":
        jack.pencolor(get_random_color())

    jack.pendown()
    jack.speed(0)
    for i in range(4):
        jack.forward(350)
        jack.right(90)
    for i in range(2):
        jack.forward(340)
        jack.right(90)
    for i in range(1):
        jack.forward(30)
        jack.right(90)
        jack.forward(340)
        jack.left(90)
        jack.forward(30)
        jack.left(90)
        jack.forward(340)
    for i in range(4):
        jack.right(90)
        jack.forward(30)
        jack.right(90)
        jack.forward(340)
        jack.left(90)
        jack.forward(30)
        jack.left(90)
        jack.forward(340)
    jack.right(90)
    jack.forward(30)
    jack.right(90)
    jack.forward(340)

    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
