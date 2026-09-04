import turtle

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-300, 200)
border.pendown()
border.pensize(3)
border.goto(300, 200)
border.goto(300, -200)
border.goto(-300, -200)
border.goto(-300, 200)
border.hideturtle()

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(stretch_wid=10, stretch_len=1)
paddle1.penup()
paddle1.goto(-260, 0)

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.shapesize(stretch_wid=10, stretch_len=1)
paddle2.penup()
paddle2.goto(260, 0)

ball  = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

score_1 = 0
score_2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 220)
score.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

def paddle1_up():
    y = paddle1.ycor()
    if y < 100:
        y += 20
        paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    if y > -100:
        y -= 20
        paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    if y < 100:
        y += 20
        paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    if y > -100:
        y -= 20
        paddle2.sety(y)

window.listen()
window.onkeypress(paddle1_up, "w")
window.onkeypress(paddle1_down, "s")
window.onkeypress(paddle2_up, "Up")
window.onkeypress(paddle2_down, "Down")

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 185:
        ball.sety(185)
        ball.dy *= -1

    if ball.ycor() < -185:
        ball.sety(-185)
        ball.dy *= -1

    if ball.xcor() > 290:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -290:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    if (ball.xcor() >= 240 and ball.xcor() <= 255) and (ball.ycor() <= paddle2.ycor() + 125 and ball.ycor() >= paddle2.ycor() - 125):
        if ball.dx > 0:
            ball.setx(240)
            ball.dx *= -1

    if (ball.xcor() <= -240 and ball.xcor() >= -255) and (ball.ycor() <= paddle1.ycor() + 125 and ball.ycor() >= paddle1.ycor() - 125):
        if ball.dx < 0:
            ball.setx(-240)
            ball.dx *= -1
