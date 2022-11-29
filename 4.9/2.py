import turtle
armi = turtle.Turtle()
def draw_sqr(name,size):
    for i in range(4):
        name.forward(size)
        name.left(90)
    name.penup()
    name.backward(10)
    name.right(90)
    name.forward(10)
    name.left(90)
    name.pendown()

window = turtle.Screen()
window.bgcolor('blue')
window.title("conc_sqr")

x = turtle.Turtle()
x.color('hotpink')
x.pensize(3)

for i in range(5):
    draw_sqr(x,20 + 20*i)

window.mainloop()