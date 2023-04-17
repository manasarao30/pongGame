from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")


screen.tracer(0)
screen.listen()

rpaddle=Paddle((350,0))
lpaddle=Paddle((-350,0))
ball=Ball()
score=ScoreBoard()


screen.onkey(rpaddle.go_up,"Up")
screen.onkey(rpaddle.go_down,"Down")
screen.onkey(lpaddle.go_up,"w")
screen.onkey(lpaddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #Detect collision with the paddle
    if ball.distance(rpaddle)<50 and ball.xcor()>320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect if right paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()

    #Detect if right paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()