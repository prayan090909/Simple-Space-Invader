import turtle
import os
import math
import random
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("red")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

player = turtle.Turtle()
player.speed(0)
player.color("blue")
player.shape("triangle")
player.penup()
player.setposition(0,-250)
player.setheading(90)

number_of_enemies = 5

enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.color("yellow")
    enemy.shape("circle")
    enemy.penup()
    x = random.randint(-200 , 200)
    y = random.randint(100,250)
    enemy.setposition(x,y)

bullet = turtle.Turtle()
bullet.speed(0)
bullet.color("white")
bullet.shape("triangle")
bullet.shapesize(0.5,0.5)
bullet.penup()
bullet.setposition(-200,250)
bullet.setheading(90)
bullet.hideturtle()

playerspeed = 15
enemyspeed= 2
bulletspeed = 20

bulletstate = "ready"
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()
def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor() , 2) + math.pow(t1.ycor() - t2.ycor() , 2))
    if distance < 15:
        return True
    return False
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")
#Main Game Loop
while True:
        for enemy in enemies:
            x = enemy.xcor()
            x += enemyspeed
            enemy.setx(x)
            if enemy.xcor() > 280:
                y = enemy.ycor()
                y -= 40
                enemyspeed *= -1
                enemy.sety(y)
            if enemy.xcor() < -280:
                y = enemy.ycor()
                y -= 40
                enemyspeed *= -1
                enemy.sety(y)
            if isCollision(bullet,enemy):
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0,-400)

                enemy.setposition(-200,250)
            
            if isCollision(enemy,player):
                enemy.hideturtle()
                player.hideturtle()
                print("Game Over")
                break
        if bulletstate == "fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"
    
