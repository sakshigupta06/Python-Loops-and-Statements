# only second side blue
import turtle
amy=turtle.Turtle()
amy.color("yellow")
amy.width(5)

for side in range(4):
    if side==1:
        amy.color("blue")
    if side==2:
        amy.color("yellow") #if is used twice and its not the efficient way
    amy.forward(100)  
    amy.right(90)  
# third and fourth side blues
import turtle
amy=turtle.Turtle()
amy.color("yellow")
amy.width(5)

for side in range(4):
    if side==2:
        amy.color("blue")
    if side==3:
        amy.color("blue")
    amy.forward(100)  
    amy.right(90)  