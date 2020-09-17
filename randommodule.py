import turtle
import random
colors=["red","cyan","yellow","white","orange"]
for steps in range(100):
    t=turtle.Turtle()
    t.width(20)
    angle= random.randint(-90,90)
    color=random.choice(colors)
    t.color(color)
    t.right(angle)
    t.forward(50)


