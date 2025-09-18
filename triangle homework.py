import turtle

t = turtle.Turtle()

def triangle():
    for change in range(3):
        t.forward(100)
        t.right(120)
        
triangle()
t.left(180)
def pentagon():
    for change in range(5):
        t.forward(200)
        t.right(72)
        
pentagon()

t.forward(200)

def hexagon():
    t.fillcolor("blue")
    t.begin_fill()
    for change in range(6):
        t.forward(50)
        t.left(60)

hexagon()
t.end_fill()
t.pencolor("blue")
t.left(50)
t.forward(20)
t.right(90)

def hide():
    for change in range(50):
        t.forward(1)
        t.right(90)
        
hide()

t.clear()
t.left(40)

def rectangle():
    for change in range(2):
        t.forward(300)
        t.right(90)
        t.forward(150)
        t.right(90)
        
rectangle()
t.right(35)
def triangle2():
    for change in range(2):
        t.forward(183)
        t.left(69.5)
        
triangle2()