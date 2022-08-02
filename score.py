from turtle import *

class Score(Turtle):

    def __init__(self):
        super().__init__()
        global p1_score
        global p2_score
        p1_score = 0
        p2_score = 0
        self.hideturtle()
        self.speed("fastest")
        self.pencolor("white")
        self.penup()
        self.goto(150, 300)
        self.write(p1_score, align='center', font=('Arial', 15, 'normal'))
        self.goto(-150, 300)
        self.write(p2_score, align='center', font=('Arial', 15, 'normal'))

    def increase_score_p1(self):

        global p1_score

        p1_score += 1

        self.goto(-150, 300)
        self.write(p1_score, align='center', font=('Arial', 20, 'normal'))
    def increase_score_p2(self):

        global p2_score
        p2_score += 1
        self.goto(150, 300)
        self.write(p2_score, align='center', font=('Arial', 20, 'normal'))


