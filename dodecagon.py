import turtle
amy=turtle.Turtle()
amy.width(5)
for side in range(12):
    if side%3==0:
        amy.color("red")
    if side%3==1:
        amy.color("orange")
    if side%3==2:
        amy.color("yellow")
     
    amy.forward(50)
    amy.right(30)