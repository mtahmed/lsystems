import math
import sys
import turtle

from  lsystem import *

class DragonLSystem(LSystem):
    def __init__(self):
        super(DragonLSystem, self).__init__("LFX", {"X":"X+YF", "Y":"FX-Y", "L":"CL"})

    def draw(self):
        super(DragonLSystem, self).draw()

        turtle.setup(800,600)
        wn = turtle.Screen()
        wn.bgcolor('lightblue')
        wn.title("Wingled Dragon")

        self.turtle = turtle.Turtle()
        self.turtle.shape('blank')
        turtle.tracer(int(sys.argv[2]),25)
        t = self.turtle
        t.reset()

        t.penup()
        t.setpos(-200,0)
        t.pendown()
        i = 200.0
        for c in self.state:
            if c == "F":
                t.forward(math.ceil(i))
            elif c == "+":
                t.right(90)
            elif c == "-":
                t.left(90)
            elif c == "C":
                i = i/math.sqrt(2)
                t.left(45)

        wn.exitonclick()

if __name__ == '__main__':
    dragon = DragonLSystem()
    dragon.step_n(int(sys.argv[1]))
    dragon.draw()
