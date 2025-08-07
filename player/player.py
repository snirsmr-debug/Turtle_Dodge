import turtle

class Player:
    def __init__(self, window_width, window_height):
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.goto(0, -window_height // 2 + 50)
        self.turtle.speed(0)
        self.window_width = window_width
        self.window_height = window_height
        self.int_speed_movment = 7

    def move_left(self):
        x = self.turtle.xcor() - 30
        if x > -self.window_width // 2 + self.int_speed_movment:
            self.turtle.setx(x)

    def move_right(self):
        x = self.turtle.xcor() + 30
        if x < self.window_width // 2 - self.int_speed_movment:
            self.turtle.setx(x)

    def move_up(self):
        y = self.turtle.ycor() + 30
        if y < self.window_height // 2 - self.int_speed_movment:
            self.turtle.sety(y)

    def move_down(self):
        y = self.turtle.ycor() - 30
        if y > -self.window_height // 2 + self.int_speed_movment:
            self.turtle.sety(y)