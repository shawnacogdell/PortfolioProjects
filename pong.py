import turtle
import os

win = turtle.Screen()
win.title("Pong by Shawna C")
win.bgcolor("forestGreen")
win.setup(width=800, height=600)
win.tracer(0)

# score
score_left = 0
score_right = 0

# paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.color("BlanchedAlmond")
paddle_left.penup()
paddle_left.goto(-350, 0)

# paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.color("BlanchedAlmond")
paddle_right.penup()
paddle_right.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("BlanchedAlmond")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# functions!
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)


# left paddle
def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)


# right paddle
def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)


def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)


# binding keys
win.listen()
win.onkeypress(paddle_left_up, "w")
win.onkeypress(paddle_left_down, "s")
win.onkeypress(paddle_right_up, "Up")
win.onkeypress(paddle_right_down, "Down")

# main loop
while True:
    win.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    # top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        pen.clear()
        pen.write(
            "Player A: {}  Player B: {}".format(score_left, score_right),
            align="center",
            font=("Courier", 24, "normal"),
        )
    # left
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        pen.clear()
        pen.write(
            "Player A: {}  Player B: {}".format(score_left, score_right),
            align="center",
            font=("Courier", 24, "normal"),
        )

    # paddle bounce
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
        ball.ycor() < paddle_right.ycor() + 40
        and ball.ycor() > paddle_right.ycor() - 40
    ):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
        ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40
    ):
        ball.setx(-340)
        ball.dx *= -1

    # computer player
    if paddle_right.ycor() < ball.ycor() and abs(paddle_right.ycor() - ball.ycor()) > 15:
        paddle_right_up()

    elif paddle_right.ycor() > ball.ycor() and abs(paddle_right.ycor() - ball.ycor()) > 15:
        paddle_right_down()
