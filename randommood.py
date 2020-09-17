# Solution — Random moods!

import turtle
import random
riley = turtle.Turtle()
riley.width(5)

mood = random.choice(["happy", "sad", "angry", "party"])

if mood == "happy":
    riley.color("yellow")
elif mood == "sad":
    riley.color("blue")
elif mood == "angry":
    riley.color("red")
elif mood == "party":
    riley.color("magenta")
else:
    riley.color("gray")

for side in range(5):
    riley.forward(100)
    riley.right(144)