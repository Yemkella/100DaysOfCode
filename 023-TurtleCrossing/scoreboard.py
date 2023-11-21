from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    
    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 250)
        self.write("Level: ", align="center", font=FONT)
        self.goto(-170, 250)
        self.write(self.level, align="center", font=FONT)


    def level_up(self):
        self.level += 1        


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
        self.goto(-220, 250)
        self.write("Level: ", align="center", font=FONT)
        self.goto(-170, 250)
        self.write(self.level, align="center", font=FONT)