from turtle import *

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        global xpos
        global ypos
        xpos = self.xcor()
        ypos = self.ycor()
        self.setheading(45)

    def ball_move(self):
        self.forward(10)

    def ball_bounce_roof(self):
        if self.heading()>0 and self.heading()<90:
            self.setheading(315)
        elif self.heading()>90 and self.heading()<180:
            self.setheading(225)

    def ball_bounce_floor(self):
        if self.heading()>270:
            self.setheading(45)
        elif self.heading()>180 and self.heading()<270:
            self.setheading(135)
    def right_wall(self):
        if self.heading()>0 and self.heading()<90:
            self.setheading(135)
        elif self.heading()>270:
            self.setheading(225)

    def left_wall(self):
        if self.heading()>180 and self.heading()<270:
            self.setheading(315)
        elif self.heading()>90 and self.heading()<180:
            self.setheading(45)
    def rest(self):
        self.goto(0,0)

