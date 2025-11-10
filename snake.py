from turtle import Turtle

X_COR = [(0 , 0) , (-20 , 0) , (-40 , 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in X_COR:
            self.add_segment(position)
            

    def add_segment(self , position):
        new_segement = Turtle("square")
        new_segement.color("white")
        new_segement.penup()
        new_segement.goto(position)
        new_segement.speed(1)
        self.segments.append(new_segement)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for seg in range(len(self.segments) -1 , 0 , -1):
            new_pos = self.segments[seg -1].pos()
            self.segments[seg].goto(new_pos)
        self.segments[0].fd(MOVE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)


    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()