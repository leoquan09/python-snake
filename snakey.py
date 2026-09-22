from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for i in STARTING_POSITIONS:
            new_t = Turtle("square")
            new_t.color("white")
            new_t.penup()
            new_t.goto(i)
            self.segments.append(new_t)

    def reset_self(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
            seg.hideturtle()

        self.segments.clear()

        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def add_segment(self, position):
        new_t = Turtle("square")
        new_t.color("white")
        new_t.penup()
        new_t.goto(position)
        self.segments.append(new_t)

    def extend(self):
        self.add_segment(self.segments[-1].position())
