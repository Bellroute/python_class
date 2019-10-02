import turtle

turtle.pensize(3) # Set pen thickness to 3 pixels
turtle.penup() # Pull the pen up
turtle.goto(-200, -50)  
turtle.pendown() # Pull the pen down
turtle.begin_fill()
turtle.color('red')
turtle.circle(40, steps = 3) # Draw a triangle
turtle.end_fill()

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color('blue')
turtle.circle(40, steps = 4) # Draw a square 13
turtle.end_fill()

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color('green')
turtle.circle(40, steps = 5) # Draw a pentagon 18
turtle.end_fill()

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color('yellow')
turtle.circle(40, steps = 6) # Draw a hexagon 23
turtle.end_fill()

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color('purple')
turtle.circle(40) # Draw a circle
turtle.end_fill()

turtle.done()
