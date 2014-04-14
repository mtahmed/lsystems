import sys
import turtle

from  lsystem import *

class TriforceLSystem(LSystem):
    def __init__(self):
        super(TriforceLSystem, self).__init__("X", {"X":"FF-[FX]+[FX]+[FX]", "F":"FF"})

    def draw(self):
        super(TriforceLSystem, self).draw()

        turtle.setup(800,600)
        wn = turtle.Screen()
        wn.bgcolor('lightblue')
        wn.title("Wingled Dragon")

        self.turtle = turtle.Turtle()
        self.turtle.shape('blank')
        self.turtle.tracer(50,0)
        t = self.turtle
        t.reset()

        stack = []
        t.penup()
        t.setpos(0,-280)
        t.pendown()
        t.left(90)
        for c in self.state:
            if c == "F":
                t.forward(1)
            elif c == "+":
                t.right(120)
            elif c == "-":
                t.left(120)
            elif c == "[":
                stack.append((t.pos(),t.heading()))
            elif c == "]":
                ((x,y), h) = stack.pop()
                t.penup()
                t.setpos(x,y)
                t.setheading(h)
                t.pendown()


        wn.exitonclick()

if __name__ == '__main__':
    plant = TriforceLSystem()
    plant.step_n(int(sys.argv[1]))
    plant.draw()
