from Shapes import *

def demo():
    r = Square(40, Vector(0, 100), color="blue")
    for i in range(6):
        for j in range(6):
            r.render()
            r.rotate(60, r.center)
        r.scale(1.1)
        r.rotate(60)
    c = Circle(Vector(0, 250), 50, color = "red")
    for i in range(6):
        c.render()
        c.rotate(60)
        c.scale(0.8)

demo()