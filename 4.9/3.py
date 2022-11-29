import turtle
armi=turtle.Turtle()
n_sides=7
l_sides=95
for i in range(n_sides):
    armi.forward(l_sides)
    armi.right(360/n_sides)