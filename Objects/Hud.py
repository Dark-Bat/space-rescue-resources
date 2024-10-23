from GameFrame import TextObject, Globals

class Score(TextObject):
    #class for displaying score
    def __init__(self, room, x: int, y: int, text='Not Set'):
        TextObject.__init__(self, room, x, y, text)
        
        #set values
        self.size = 60
        self.font = "Arial Black"
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()

    def update_score(self, change):
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()