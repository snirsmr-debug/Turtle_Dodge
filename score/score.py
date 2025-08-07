import turtle

class ScoreDisplay:
    def __init__(self, window_height):
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.color("white")
        self.pen.penup()
        self.pen.goto(0, window_height // 2 - 40)

    def update(self, score):
        self.pen.clear()
        self.pen.write(f"Score: {score}", align="center", font=("Arial", 18, "bold"))