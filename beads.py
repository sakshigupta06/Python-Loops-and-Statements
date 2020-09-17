import turtle
amy=turtle.Turtle()
def beads(amy):
    
# Draw ten beads.
 
    for n in range(10):
        for side in range(6):
            if n % 2 == 0:
                amy.color("red")
            else:
                amy.color("blue")
               
        amy.forward(100)
        amy.right(60)
beads(amy)
amy.forward(40)     

