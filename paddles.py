from turtle import *

class Paddle(Turtle):

    def __init__(self):
        super(Paddle, self).__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(1,5)
        self.setheading(90)
        self.penup()
        self.goto(-470,0)
        self.showturtle()
    def set_player_2(self):
        self.goto(470,0)

    def up(self):
        self.setheading(90)
        if self.ycor()<350:
            self.forward(25)
    def down(self):
        self.setheading(270)
        if self.ycor() > -350:
            self.forward(25)
