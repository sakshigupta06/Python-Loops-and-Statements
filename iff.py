# It makes the fourth side blue.
import turtle
jack = turtle.Turtle()
jack.color("yellow")

for side in range(4):
    if side == 3:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)



    # The whole square would be yellow, because it would not change the color to blue until after drawing the fourth side.
import turtle
jack = turtle.Turtle()
jack.color("yellow")

for side in range(4):
    jack.forward(100)
    jack.right(90)
    if side == 3:
        jack.color("blue")

        # It makes both the third and fourth sides blue.
import turtle
jack = turtle.Turtle()
jack.color("yellow")

for side in range(4):
    if side == 2:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)