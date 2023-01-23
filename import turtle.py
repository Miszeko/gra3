import turtle


#okno
wn = turtle.Screen() 
wn.title("gra") 
wn.bgcolor("lightblue") 
wn.setup(width=1900, height=1000) 
wn.tracer(0) 

# punkty
score = 0  

# paletka 
pad_a = turtle.Turtle() 
pad_a.speed(0) 
pad_a.shape("square") 
pad_a.color("red") 
pad_a.shapesize(stretch_wid=0.8,stretch_len=10.2) 
pad_a.penup() 
pad_a.goto(0, -420) 

t = turtle.Turtle()
t.speed(0)
t.shape("square")
t.color("white")
t.shapesize(stretch_wid=3,stretch_len=3)
t.penup()
t.goto(-850, 350)

t1 = turtle.Turtle()
t1.speed(0)
t1.shape("square")
t1.color("green")
t1.shapesize(stretch_wid=3,stretch_len=3)
t1.penup()
t1.goto(10, 0)

t2 = turtle.Turtle()
t2.speed(0)
t2.shape("square")
t2.color("white")
t2.shapesize(stretch_wid=3,stretch_len=3)
t2.penup()
t2.goto(-760, 350)

t3 = turtle.Turtle()
t3.speed(0)
t3.shape("square")
t3.color("white")
t3.shapesize(stretch_wid=3,stretch_len=3)
t3.penup()
t3.goto(-670, 350)

t4 = turtle.Turtle()
t4.speed(0)
t4.shape("square")
t4.color("white")
t4.shapesize(stretch_wid=3,stretch_len=3)
t4.penup()
t4.goto(-580, 350)

t5 = turtle.Turtle()
t5.speed(0)
t5.shape("square")
t5.color("white")
t5.shapesize(stretch_wid=3,stretch_len=3)
t5.penup()
t5.goto(-490, 350)

t6 = turtle.Turtle()
t6.speed(0)
t6.shape("square")
t6.color("white")
t6.shapesize(stretch_wid=3,stretch_len=3)
t6.penup()
t6.goto(-400, 350)

t7 = turtle.Turtle()
t7.speed(0)
t7.shape("square")
t7.color("white")
t7.shapesize(stretch_wid=3,stretch_len=3)
t7.penup()
t7.goto(-310, 350)

t8 = turtle.Turtle()
t8.speed(0)
t8.shape("square")
t8.color("white")
t8.shapesize(stretch_wid=3,stretch_len=3)
t8.penup()
t8.goto(-220, 350)
t9 = turtle.Turtle()
t9.speed(0)
t9.shape("square")
t9.color("white")
t9.shapesize(stretch_wid=3,stretch_len=3)
t9.penup()
t9.goto(-130, 350)

t10 = turtle.Turtle()
t10.speed(0)
t10.shape("square")
t10.color("white")
t10.shapesize(stretch_wid=3,stretch_len=3)
t10.penup()
t10.goto(-40, 350)

t11 = turtle.Turtle()
t11.speed(0)
t11.shape("square")
t11.color("white")
t11.shapesize(stretch_wid=3,stretch_len=3)
t11.penup()
t11.goto(50, 350)

t12 = turtle.Turtle()
t12.speed(0)
t12.shape("square")
t12.color("white")
t12.shapesize(stretch_wid=3,stretch_len=3)
t12.penup()
t12.goto(140, 350)

t13 = turtle.Turtle()
t13.speed(0)
t13.shape("square")
t13.color("white")
t13.shapesize(stretch_wid=3,stretch_len=3)
t13.penup()
t13.goto(220, 350)

t14 = turtle.Turtle()
t14.speed(0)
t14.shape("square")
t14.color("white")
t14.shapesize(stretch_wid=3,stretch_len=3)
t14.penup()
t14.goto(310, 350)

t15 = turtle.Turtle()
t15.speed(0)
t15.shape("square")
t15.color("white")
t15.shapesize(stretch_wid=3,stretch_len=3)
t15.penup()
t15.goto(400, 350)

t16 = turtle.Turtle()
t16.speed(0)
t16.shape("square")
t16.color("white")
t16.shapesize(stretch_wid=3,stretch_len=3)
t16.penup()
t16.goto(490, 350)

t17 = turtle.Turtle()
t17.speed(0)
t17.shape("square")
t17.color("white")
t17.shapesize(stretch_wid=3,stretch_len=3)
t17.penup()
t17.goto(580, 350)

t18 = turtle.Turtle()
t18.speed(0)
t18.shape("square")
t18.color("white")
t18.shapesize(stretch_wid=3,stretch_len=3)
t18.penup()
t18.goto(670, 350)

t19 = turtle.Turtle()
t19.speed(0)
t19.shape("square")
t19.color("white")
t19.shapesize(stretch_wid=3,stretch_len=3)
t19.penup()
t19.goto(760, 350)

t20 = turtle.Turtle()
t20.speed(0)
t20.shape("square")
t20.color("white")
t20.shapesize(stretch_wid=3,stretch_len=3)
t20.penup()
t20.goto(760, 350)

t21 = turtle.Turtle()
t21.speed(0)
t21.shape("square")
t21.color("white")
t21.shapesize(stretch_wid=3,stretch_len=3)
t21.penup()
t21.goto(-760, 260)

t22 = turtle.Turtle()
t22.speed(0)
t22.shape("square")
t22.color("white")
t22.shapesize(stretch_wid=3,stretch_len=3)
t22.penup()
t22.goto(-670, 260)

t23 = turtle.Turtle()
t23.speed(0)
t23.shape("square")
t23.color("white")
t23.shapesize(stretch_wid=3,stretch_len=3)
t23.penup()
t23.goto(-580, 260)

t24 = turtle.Turtle()
t24.speed(0)
t24.shape("square")
t24.color("white")
t24.shapesize(stretch_wid=3,stretch_len=3)
t24.penup()
t24.goto(-490, 260)

t25 = turtle.Turtle()
t25.speed(0)
t25.shape("square")
t25.color("white")
t25.shapesize(stretch_wid=3,stretch_len=3)
t25.penup()
t25.goto(-400, 260)

t26 = turtle.Turtle()
t26.speed(0)
t26.shape("square")
t26.color("white")
t26.shapesize(stretch_wid=3,stretch_len=3)
t26.penup()
t26.goto(-310, 260)

t27 = turtle.Turtle()
t27.speed(0)
t27.shape("square")
t27.color("white")
t27.shapesize(stretch_wid=3,stretch_len=3)
t27.penup()
t27.goto(-220, 260)

t28 = turtle.Turtle()
t28.speed(0)
t28.shape("square")
t28.color("white")
t28.shapesize(stretch_wid=3,stretch_len=3)
t28.penup()
t28.goto(-130, 260)

t29 = turtle.Turtle()
t29.speed(0)
t29.shape("square")
t29.color("white")
t29.shapesize(stretch_wid=3,stretch_len=3)
t29.penup()
t29.goto(-40, 260)

t30 = turtle.Turtle()
t30.speed(0)
t30.shape("square")
t30.color("white")
t30.shapesize(stretch_wid=3,stretch_len=3)
t30.penup()
t30.goto(50, 260)

t31 = turtle.Turtle()
t31.speed(0)
t31.shape("square")
t31.color("white")
t31.shapesize(stretch_wid=3,stretch_len=3)
t31.penup()
t31.goto(140, 260)

t32 = turtle.Turtle()
t32.speed(0)
t32.shape("square")
t32.color("white")
t32.shapesize(stretch_wid=3,stretch_len=3)
t32.penup()
t32.goto(220, 260)

t33 = turtle.Turtle()
t33.speed(0)
t33.shape("square")
t33.color("white")
t33.shapesize(stretch_wid=3,stretch_len=3)
t33.penup()
t33.goto(310, 260)

t34 = turtle.Turtle()
t34.speed(0)
t34.shape("square")
t34.color("white")
t34.shapesize(stretch_wid=3,stretch_len=3)
t34.penup()
t34.goto(400, 260)

t35 = turtle.Turtle()
t35.speed(0)
t35.shape("square")
t35.color("white")
t35.shapesize(stretch_wid=3,stretch_len=3)
t35.penup()
t35.goto(490, 260)

t36 = turtle.Turtle()
t36.speed(0)
t36.shape("square")
t36.color("white")
t36.shapesize(stretch_wid=3,stretch_len=3)
t36.penup()
t36.goto(580, 260)

t37 = turtle.Turtle()
t37.speed(0)
t37.shape("square")
t37.color("white")
t37.shapesize(stretch_wid=3,stretch_len=3)
t37.penup()
t37.goto(670, 260)

t38 = turtle.Turtle()
t38.speed(0)
t38.shape("square")
t38.color("white")
t38.shapesize(stretch_wid=3,stretch_len=3)
t38.penup()
t38.goto(760, 260)

t39 = turtle.Turtle()
t39.speed(0)
t39.shape("square")
t39.color("white")
t39.shapesize(stretch_wid=3,stretch_len=3)
t39.penup()
t39.goto(760, 260)

t40 = turtle.Turtle()
t40.speed(0)
t40.shape("square")
t40.color("white")
t40.shapesize(stretch_wid=3,stretch_len=3)
t40.penup()
t40.goto(-850, 260)

t41 = turtle.Turtle()
t41.speed(0)
t41.shape("square")
t41.color("white")
t41.shapesize(stretch_wid=3,stretch_len=3)
t41.penup()
t41.goto(-760, 170)

t42 = turtle.Turtle()
t42.speed(0)
t42.shape("square")
t42.color("white")
t42.shapesize(stretch_wid=3,stretch_len=3)
t42.penup()
t42.goto(-670, 170)

t43 = turtle.Turtle()
t43.speed(0)
t43.shape("square")
t43.color("white")
t43.shapesize(stretch_wid=3,stretch_len=3)
t43.penup()
t43.goto(-580, 170)

t44 = turtle.Turtle()
t44.speed(0)
t44.shape("square")
t44.color("white")
t44.shapesize(stretch_wid=3,stretch_len=3)
t44.penup()
t44.goto(-490, 170)

t45 = turtle.Turtle()
t45.speed(0)
t45.shape("square")
t45.color("white")
t45.shapesize(stretch_wid=3,stretch_len=3)
t45.penup()
t45.goto(-400, 170)

t46 = turtle.Turtle()
t46.speed(0)
t46.shape("square")
t46.color("white")
t46.shapesize(stretch_wid=3,stretch_len=3)
t46.penup()
t46.goto(-310, 170)

t47 = turtle.Turtle()
t47.speed(0)
t47.shape("square")
t47.color("white")
t47.shapesize(stretch_wid=3,stretch_len=3)
t47.penup()
t47.goto(-220, 170)

t48 = turtle.Turtle()
t48.speed(0)
t48.shape("square")
t48.color("white")
t48.shapesize(stretch_wid=3,stretch_len=3)
t48.penup()
t48.goto(-130, 170)

t49 = turtle.Turtle()
t49.speed(0)
t49.shape("square")
t49.color("white")
t49.shapesize(stretch_wid=3,stretch_len=3)
t49.penup()
t49.goto(-40, 170)

t50 = turtle.Turtle()
t50.speed(0)
t50.shape("square")
t50.color("white")
t50.shapesize(stretch_wid=3,stretch_len=3)
t50.penup()
t50.goto(50, 170)

t51 = turtle.Turtle()
t51.speed(0)
t51.shape("square")
t51.color("white")
t51.shapesize(stretch_wid=3,stretch_len=3)
t51.penup()
t51.goto(140, 170)

t52 = turtle.Turtle()
t52.speed(0)
t52.shape("square")
t52.color("white")
t52.shapesize(stretch_wid=3,stretch_len=3)
t52.penup()
t52.goto(220, 170)

t53 = turtle.Turtle()
t53.speed(0)
t53.shape("square")
t53.color("white")
t53.shapesize(stretch_wid=3,stretch_len=3)
t53.penup()
t53.goto(310, 170)

t54 = turtle.Turtle()
t54.speed(0)
t54.shape("square")
t54.color("white")
t54.shapesize(stretch_wid=3,stretch_len=3)
t54.penup()
t54.goto(400, 170)

t55 = turtle.Turtle()
t55.speed(0)
t55.shape("square")
t55.color("white")
t55.shapesize(stretch_wid=3,stretch_len=3)
t55.penup()
t55.goto(490, 170)

t56 = turtle.Turtle()
t56.speed(0)
t56.shape("square")
t56.color("white")
t56.shapesize(stretch_wid=3,stretch_len=3)
t56.penup()
t56.goto(580, 170)

t57 = turtle.Turtle()
t57.speed(0)
t57.shape("square")
t57.color("white")
t57.shapesize(stretch_wid=3,stretch_len=3)
t57.penup()
t57.goto(670, 170)

t58 = turtle.Turtle()
t58.speed(0)
t58.shape("square")
t58.color("white")
t58.shapesize(stretch_wid=3,stretch_len=3)
t58.penup()
t58.goto(760, 170)

t59 = turtle.Turtle()
t59.speed(0)
t59.shape("square")
t59.color("white")
t59.shapesize(stretch_wid=3,stretch_len=3)
t59.penup()
t59.goto(760, 170)

t60 = turtle.Turtle()
t60.speed(0)
t60.shape("square")
t60.color("white")
t60.shapesize(stretch_wid=3,stretch_len=3)
t60.penup()
t60.goto(-850, 170)

# piłka
ball = turtle.Turtle() 
ball.speed(0) 
ball.shape("classic")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.9 
ball.dy = 0.9 

# tekst
pen = turtle.Turtle() 
pen.speed(0) 
pen.shape("square") 
pen.color("black") 
pen.penup() 
pen.hideturtle()
pen.goto(0, 445) 
pen.write("punkty: 0", align="center", font=("Courier", 16, "normal")) 

# Poruszanie sie platform
def pad_a_left():
    x = pad_a.xcor() 
    x -= 55
    pad_a.setx(x)

def pad_a_right():
    x = pad_a.xcor() 
    x += 55
    pad_a.setx(x)

# Klawisze
wn.listen()
wn.onkeypress(pad_a_left, "a")
wn.onkeypress(pad_a_right, "d")


# pętla
while True:
    wn.update()
    
    # ruch piłki
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor() + ball.dy) 


       #zablokowanie paletki
    if pad_a.xcor() > 945:  
        pad_a.setx(945)

    elif pad_a.xcor() < -945:  
        pad_a.setx(-945)
      
    # granice mapy

    # górna ściana
    if ball.ycor() > 495:  
        ball.sety(495) 
        ball.dy *= -1
    
    elif ball.ycor() < -495:
        ball.goto(0, 0)

    # lewa ściana i prawa ściana
    if ball.xcor() > 945:  
        ball.setx(945)
        ball.dx *= -1

    elif ball.xcor() < -945:
        ball.setx(-945)
        ball.dx *= -1

    # zderzanie sie piłki z paletką
    if ball.ycor() < -420 and ball.xcor() < pad_a.xcor() + 100 and ball.xcor() > pad_a.xcor() - 100: 
        ball.dy *= -1

    elif ball.distance(t) <60:
        t.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t1) <60:
        t1.goto(10000, 1000)
        ball.dy *= -1

    elif ball.distance(t2) <60:
        t2.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t3) <60:
        t3.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t4) <60:
        t4.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t5) <60:
        t5.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t6) <60:
        t6.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t7) <60:
        t7.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t8) <60:
        t8.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t9) <60:
        t9.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1    
    
    elif ball.distance(t10) <60:
        t10.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t11) <60:
        t11.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t12) <60:
        t12.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t13) <60:
        t13.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t14) <60:
        t14.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t15) <60:
        t15.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t16) <60:
        t16.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t17) <60:
        t17.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t18) <60:
        t18.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t19) <60:
        t19.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t20) <60:
        t20.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t21) <60:
        t21.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t22) <60:
        t22.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t23) <60:
        t23.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t24) <60:
        t24.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t25) <60:
        t25.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t26) <60:
        t26.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t27) <60:
        t27.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t28) <60:
        t28.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1    
    
    elif ball.distance(t29) <60:
        t29.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t30) <60:
        t30.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t31) <60:
        t31.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t32) <60:
        t32.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t33) <60:
        t33.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t34) <60:
        t34.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t35) <60:
        t35.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t36) <60:
        t36.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t37) <60:
        t37.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t38) <60:
        t38.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t39) <60:
        t39.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t40) <60:
        t40.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1
   
    elif ball.distance(t41) <60:
        t41.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t42) <60:
        t42.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t43) <60:
        t43.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t44) <60:
        t44.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t45) <60:
        t45.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t46) <60:
        t46.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t47) <60:
        t47.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t48) <60:
        t48.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1    
    
    elif ball.distance(t49) <60:
        t49.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t50) <60:
        t50.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t51) <60:
        t51.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t52) <60:
        t52.goto(10000, 1000)
        score += 1
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t53) <60:
        t53.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t54) <60:
        t54.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t55) <60:
        t55.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t56) <60:
        t56.goto(10000, 1000)
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t57) <60:
        t57.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t58) <60:
        t58.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t59) <60:
        t59.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1

    elif ball.distance(t60) <60:
        t60.goto(10000, 1000)
        score += 1 
        pen.clear()
        pen.write("punkty: {}".format(score), align="center", font=("Courier", 16, "normal"))
        ball.dy *= -1
    
    if score == 60:
        pen.showturtle()
        pen.goto(0, 0) 
        pen.write("YOU WON!", align="center", font=("Courier", 60, "normal")) 
 