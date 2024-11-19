from GameFrame import TextObject, Globals, RoomObject

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
        #allows the score of the player to change throughout the game.
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()

class Lives(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self,room,x,y)
        if Globals.LIVES <= 5:
            #set image
            self.lives_icon = []
            #load the various life images
            for index in range(6):
                self.lives_icon.append(self.load_image(f"Lives_Frames/Lives_{index}.png"))
            self.update_image()
    
    def update_image(self):
        #a function for updating the lives, useful in collision events
        self.set_image(self.lives_icon[Globals.LIVES], 125, 23)


class AstroText(TextObject):
    #A seperate class for the text on the bottom of the gameplay room
    def __init__(self, room, x: int, y: int):
        TextObject.__init__(self, room, x, y, text=str(f"{Globals.astro_count}/{Globals.threshold}"))
        
        #set values
        self.size = 40
        self.font = "Arial Black"
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()
        self.text = str(f"{Globals.astro_count}/{Globals.threshold}")

    def update_astrotext(self):
        #Changes the display depending on neccesary collection score and how many collected for victory
        self.text = str(f"{Globals.astro_count}/{Globals.threshold}")
        self.update_text()
