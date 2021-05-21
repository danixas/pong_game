import turtle

wn = turtle.Screen()
wn.title("pong game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# left paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.speed(0)
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# right paddle
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.speed(0)
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.1

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# scores
score_a = 0
score_b = 0

# functions
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# keyboard bindings
wn.listen()
wn.onkeypress(left_paddle_up, "w")
wn.onkeypress(left_paddle_down, "s")
wn.onkeypress(right_paddle_up, "Up")
wn.onkeypress(right_paddle_down, "Down")


while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check the borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # Check paddles
    if ball.xcor() > 340 and (ball.ycor() < right_paddle.ycor() + 50) and (ball.ycor() > right_paddle.ycor() - 50):
        ball.dx *= -1
    if ball.xcor() < -340 and (ball.ycor() < left_paddle.ycor() + 50) and (ball.ycor() > left_paddle.ycor() - 50):
        ball.dx *= -1