import turtle
import winsound

wn=turtle.Screen()
wn.title("Pong By Shivangini")
wn.bgcolor("black")
wn.setup(width=1000, height=800)
wn.tracer(0)

#Border
border = turtle.Turtle()
border.color('white')
border.penup()
border.goto(400,0)
border.pensize(2)
border.hideturtle()
border.pendown()
border.left(90)
border.forward(300)
border.left(90)
border.forward(800)
border.left(90)
border.forward(600)
border.left(90)
border.forward(800)
border.left(90)
border.forward(300)

#Score - Keep track of the score
score_a=0
score_b=0


#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)


#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)

#Ball
ball=turtle.Turtle()
ball.speed(0) 
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.30
ball.dy=-0.30

#Pen - used for scoring
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,305)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


#Function 
def  paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def  paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def  paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def  paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"u")
wn.onkeypress(paddle_a_down,"d")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#Main  game loop 
while True:
    wn.update()
    
    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)#yeh sound dega
    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    #Paddle and balls collisions
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


