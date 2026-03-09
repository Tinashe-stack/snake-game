from pathlib import Path
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
DATA_FILE = Path(__file__).with_name("data.txt")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def load_high_score(self):
        if not DATA_FILE.exists():
            DATA_FILE.write_text("0")
            return 0
        return int(DATA_FILE.read_text().strip() or 0)

    def save_high_score(self):
        DATA_FILE.write_text(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}  High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    
    