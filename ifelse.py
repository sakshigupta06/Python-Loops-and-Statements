import turtle
jack=turtle.Turtle()
jack.color("yellow")
for side in range(4):
    if side == 1:
        jack.color("blue")
    else:
        jack.color("yellow")
    jack.forward(100)
    jack.right(90)