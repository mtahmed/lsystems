from  lsystem import *
import turtle
import sys

class Dragon_LSystem(LSystem):
    def __init__(self):
        super(Dragon_LSystem, self).__init__("FX", {"X":"X+YF", "Y":"FX-Y"})

    def draw(self):
        super(Dragon_LSystem, self).draw()

        turtle.setup(800,600)
        wn = turtle.Screen()
        wn.bgcolor('lightblue')
        wn.title("Wingled Dragon")

        self.turtle = turtle.Turtle()
        self.turtle.shape('blank')
        self.turtle.tracer(8,25)
        t = self.turtle
        t.reset()

        t.left(90)
        for c in self.state:
            if c == "F":
                t.forward(10)
            elif c == "+":
                t.right(90)
            elif c == "-":
                t.left(90)

        wn.exitonclick()

dragon = Dragon_LSystem()
dragon.step_n(int(sys.argv[1]))
dragon.draw()
