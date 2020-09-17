import turtle
amy=turtle.Turtle()

def bead_color(num):
    if num % 3 == 0:
        return "red"
    else:
        if num % 3 == 1:
            return "green"
        else:
            return "blue"
bead_color(num)