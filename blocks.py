from turtle import Turtle
from random import choice
COLORS = ['red', 'yellow', 'green', 'blue', 'purple', 'gold']
class BlockManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.all_blocks = []


    def create_block(self, x_cor, y_cor, color):
        new_block = Turtle()
        new_block.penup()
        new_block.goto(x_cor, y_cor)
        new_block.color(COLORS[color])
        new_block.shape('square')
        new_block.shapesize(stretch_wid=2, stretch_len=4)
        self.all_blocks.append(new_block)

    def destroy_block(self, block):
        self.all_blocks.remove(block)
        block.clear()
        block.hideturtle()