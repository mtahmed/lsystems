import sys
import turtle

from  lsystem import *

class PlantLSystem(LSystem):
    def __init__(self):
        super(PlantLSystem, self).__init__("X", {"X":"F-[[X]+X]+F[+FX]-X", "F":"FF"})

    def draw(self):
        super(PlantLSystem, self).draw()

        turtle.setup(800,600)
        wn = turtle.Screen()
        wn.bgcolor('lightblue')
        wn.title("Wingled Dragon")

        self.turtle = turtle.Turtle()
        self.turtle.shape('blank')
        self.turtle.tracer(100,0)
        t = self.turtle
        t.reset()

        stack = []
        t.penup()
        t.setpos(-300,0)
        t.pendown()
        for c in self.state:
            if c == "F":
                t.forward(10)
            elif c == "+":
                t.right(25)
            elif c == "-":
                t.left(25)
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
    plant = PlantLSystem()
    plant.step_n(int(sys.argv[1]))
    plant.draw()
