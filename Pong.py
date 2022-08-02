
from score import *
from turtle import *
from paddles import *
from ball import *
import time
screen1 = Screen()
screen = Turtle()

screen1.tracer(0)
screen1.bgcolor("black")
screen1.setup(1000,800)
screen1.tracer(0)

screen.penup()
screen.hideturtle()
screen.speed("fastest")
screen.pencolor("white")
screen.pensize(5)
screen.goto(0,520)
screen.setheading(270)
screen.pendown()
score_display1 = Score()
score_display2 =Score()

while screen.ycor()>-500:
    screen.forward(20)
    screen.penup()
    screen.forward(25)
    screen.pendown()

player_1 = Paddle()
player_2 = Paddle()
player_2.set_player_2()
ball = Ball()
score_display2.clear()
screen1.update()


run_game = True

screen1.listen()
screen1.onkeypress(key="w", fun = player_1.up)
screen1.onkeypress(key="s", fun = player_1.down)
screen1.onkeypress(key="Up", fun = player_2.up)
screen1.onkeypress(key="Down", fun = player_2.down)



while run_game:
    time.sleep(0.02)




    screen1.update()

    ball.ball_move()

    print(ball.distance(player_1))
    if ball.ycor()>390:
        ball.ball_bounce_roof()
    elif ball.ycor()<-390:
        ball.ball_bounce_floor()
    elif ball.xcor()>500:
        time.sleep(1)
        score_display1.clear()
        score_display1.increase_score_p1()
        ball.right_wall()
        ball.rest()
    elif ball.xcor()<-500:
        time.sleep(1)
        score_display2.clear()
        score_display2.increase_score_p2()
        ball.left_wall()
        ball.rest()




    if ball.distance(player_2)<50 and ball.xcor()>=450:
        ball.right_wall()
    if ball.distance(player_1)<50 and ball.xcor()<=-450:
        ball.left_wall()









screen1.exitonclick()
