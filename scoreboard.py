from turtle import Turtle



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align='left', font=('Courier', 60, 'normal'))
        self.goto(100, 200)
        self.write(self.rscore, align='left', font=('Courier', 60, 'normal'))

    def l_point(self):
        self.lscore+=1
        self.update_score()

    def r_point(self):
        self.rscore+=1
        self.update_score()
