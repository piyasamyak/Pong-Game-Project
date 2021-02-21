from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        self.create_half_line()

    def create_half_line(self):
        self.goto(0, -300)
        while self.ycor() < 280:
            print(self.ycor())
            self.pendown()
            self.goto(0, self.ycor() + 20)
            self.penup()
            self.goto(0, self.ycor() + 20)

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.create_half_line()

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
