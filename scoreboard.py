from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")
HIGHSCORE_FILE_NAME = ".highscore"

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.highscore = self.read_highscore()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def read_highscore(self):
        try:
            with open(HIGHSCORE_FILE_NAME) as data:
                return int(data.read())
        except:
            with open(HIGHSCORE_FILE_NAME,mode="w") as data:
                data.write("0")
            return 0

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def save_highscore(self):
        with open(HIGHSCORE_FILE_NAME,mode="w") as data:
            data.write(f"{self.highscore}")