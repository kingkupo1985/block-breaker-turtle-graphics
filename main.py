from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import BlockManager
import time

# constructing screen
s = Screen()
s.bgcolor('black')
s.setup(width=840, height=600)
s.title('PONG by DK')
s.listen()
s.tracer(0)

# constructing paddles and ball
p1 = Paddle((0, -250)) # right paddle
b = Ball() # ball to hit
blocs = BlockManager()

# listening for key presses
s.onkey(p1.move_left, "Left")
s.onkey(p1.move_right, "Right")
s.onkey(fun=s.exitonclick, key='x')
x = 350
y = 0
c_index = 0
# game loop
while len(blocs.all_blocks) < 48:
    blocs.create_block(x, y, c_index)
    x -= 100
    if x <= -363:
        x = 350
        y += 50
        c_index += 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    s.update()
    b.move()
    # detect ceiling and walls
    if b.ycor() > 280:
        b.bounce()
    if b.xcor() > 380 or b.xcor() < -380:
        b.xbounce()
    # detect paddle and ball collision
    if b.distance(p1) < 35:
        b.bounce()
    # detect ball passed paddle and bottom
    if b.ycor() < -280:
        b.reset_ball()

    # detect ball and block collision
    for bloc in blocs.all_blocks:
        if b.distance(bloc) < 40:
            blocs.destroy_block(bloc)
            b.bounce()
            b.xbounce()

s.exitonclick()