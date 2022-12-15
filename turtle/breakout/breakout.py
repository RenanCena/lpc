import turtle

width_screen = 600
height_screen = 800

# Draw Screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width_screen, height_screen)
screen.tracer(0)

# Draw Paddle
paddle = turtle.Turtle()
paddle.shapesize(1, 5)
paddle.shape("square")
paddle.color("cyan")
paddle.penup()
paddle.goto(0, -300)

# Draw Ball
ball = turtle.Turtle()
ball.shapesize(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)


turtle.mainloop()