import turtle
armi = turtle.Turtle()
armi.speed(10)
def draw_square(turtle, size):
    for i in range(4):
        armi.forward(size)
        armi.left(90)
        armi.speed(10)

if __name__ == "__main__":
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    armi = turtle.Turtle()
    armi.color("blue")
    armi.pensize(3)
    boxes = 20

    for _ in range(boxes):
        draw_square(armi, 200)
        armi.left(360 / boxes)

    wn.mainloop()