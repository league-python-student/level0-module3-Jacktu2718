import turtle
if __name__ == '__main__':
    jack = turtle.Turtle()
    jack.shape('turtle')
    jack.color('blue', 'green')
    jack.speed(100)
    jack.pensize(2.5)
    # TODO 1) Set the X position of the turtle so that it starts on the left.
    jack.penup()
    jack.setx(-400)


    for i in range(10):
        jack.penup()
        jack.forward(50)
        jack.pendown()

        for i in range(5):
            jack.forward(30)
            jack.left(144)
    jack.penup()
    jack.forward(100)
    jack.shapesize(2.5)




    # TODO 2) Make the turtle draw a star shape. Hint: angle=144.

    # TODO 3) Set the length of each line in the star to 30

    # TODO: CHALLENGE
    #       Make the turtle draw a line of stars like the image in
    #       this folder.
    #       Hint: The distance between stars is 50.

# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
