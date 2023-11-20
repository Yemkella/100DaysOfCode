from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from playsound import playsound
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle_r = Paddle(position=(350, 0))
paddle_l = Paddle(position=(-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

game_is_on = True 
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor () < -280:
        ball.bounce()
    if ball.distance(paddle_r) < 52 and ball.xcor() > 320:
        ball.hit()
        playsound("../022-Pong/assets/hit_1.wav")
    if ball.distance(paddle_l) < 52 and ball.xcor() < -320:
        ball.hit()
        playsound("../022-Pong/assets/hit_2.wav")



    #Detect R paddle misses
    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        playsound("../022-Pong/assets/miss.wav")


    #Detect L paddle misses
    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        playsound("../022-Pong/assets/miss.wav")
        








screen.exitonclick()
