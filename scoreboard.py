from turtle import Turtle
ALLIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')



class Scoreboard(Turtle):

    def __init__(self,):
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as file:
            content =  file.read()
            if content:
                self.high_score = int(content)
            else:
                self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score:{self.high_score}', align=ALLIGNMENT, font=FONT)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    #def game_over(self):
     #   self.goto(0,0)
     #   self.write('GAME OVER', align=ALLIGNMENT, font=FONT)
        



    def add_count(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
