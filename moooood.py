#  the code with the mistake:
# it should return yellow star but it returns grey

mood = "happy"

import turtle
riley = turtle.Turtle()
riley.width(5)

if mood == "happy":
    riley.color("yellow")
if mood == "sad":
    riley.color("blue")
else:
    riley.color("gray")

for side in range(5):
    riley.forward(100)
    riley.right(144)    
    
    # Here's the solution that uses nesting:

mood = "happy"

import turtle
riley = turtle.Turtle()
riley.width(5)

if mood == "happy":
    riley.color("yellow")
else:
    if mood == "sad":
        riley.color("blue")
    else:
        riley.color("gray")

for side in range(5):
    riley.forward(100)
    riley.right(144)             

# And here's the solution that uses elif:

mood = "happy"

import turtle
riley = turtle.Turtle()
riley.width(5)

if mood == "happy":
    riley.color("yellow")
elif mood == "sad":
    riley.color("blue")
else:
    riley.color("gray")

for side in range(5):
    riley.forward(100)
    riley.right(144)



