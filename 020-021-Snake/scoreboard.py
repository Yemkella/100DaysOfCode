from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"    
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.goto(0, 275)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)


    def count(self):
        self.clear()
        self.penup()
        self.score += 1
        self.hideturtle()
        self.color("white")
        self.goto(0, 275)
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 20, "normal"))


    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", False, align="center", font=("Arial", 20, "normal"))
