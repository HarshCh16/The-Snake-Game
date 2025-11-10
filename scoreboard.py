from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier" , 20 , "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0 , 270)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   Highscore: {self.highscore}" , False , ALIGNMENT , FONT)

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt" , mode = 'w') as file:
                self.highscore = file.write(f"{self.score}")
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0 , 0)
    #     self.write("GAME OVER" , False , ALIGNMENT , FONT)
