import turtle
ablak = turtle.Screen()
ablak.bgcolor('#90EE90')
BB = turtle.Pen()
BB.shape('turtle')
BB.color('blue')
BB.stamp()
move=30
for i in range(12):
    BB.penup()
    BB.forward(50)
    BB.pendown()
    BB.forward(25)
    BB.penup()
    BB.forward(15)
    BB.stamp()
    BB.home()
    BB.right(move)
    move = move + 30
    