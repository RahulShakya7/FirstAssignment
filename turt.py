import turtle
b = turtle.Screen()
b.bgcolor("Black")
star = turtle.Turtle()
star.goto(-150, 50)
star.color("Cyan")
sides = 5
side = 300
each_angle = 720.0 / sides
for i in range(sides):
    star.forward(side)
    star.right(each_angle)



turtle.done()
