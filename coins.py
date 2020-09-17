# true or false
import turtle
t = turtle.Turtle()
t.width(100)

coins = 1000 # This is the line we changed.
rich = coins >= 1000

if rich:
    t.color("gold")
else:
    t.color("silver")

t.forward(0)