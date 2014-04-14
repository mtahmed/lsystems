from  lsystem import *
import turtle
import sys
import math

class Dragon_LSystem(LSystem):
    def __init__(self):
        super(Dragon_LSystem, self).__init__("LFX", {"X":"X+YF", "Y":"FX-Y", "L":"CL"})

    def draw(self):
        super(Dragon_LSystem, self).draw()

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

dragon = Dragon_LSystem()
dragon.step_n(int(sys.argv[1]))
dragon.draw()
