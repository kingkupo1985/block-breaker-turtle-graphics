from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, tuple_coordinates):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape('square')
        self.color('white')
        self.goto(tuple_coordinates)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.showturtle()

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())