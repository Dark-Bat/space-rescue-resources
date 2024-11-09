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
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()

class Lives(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self,room,x,y)

        #set image
        self.lives_icon = []
        #load the various life images
        for index in range(6):
            self.lives_icon.append(self.load_image(f"Lives_Frames/Lives_{index}.png"))
        self.update_image()
    
    def update_image(self):
        #updates the lives
        self.set_image(self.lives_icon[Globals.LIVES], 125, 23)

class AstroCollection(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("AstroCollection.png")
        self.depth = -1
        self.set_image(image,100,100)

    def end_game(self):
        self.room.running = False

class AstroText(TextObject):
    def __init__(self, room, x: int, y: int, text=f"{Globals.astro_count}/{Globals.threshold}"):
        TextObject.__init__(self, room, x, y, text)
        
        #set values
        self.size = 40
        self.font = "Arial Black"
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()

    def update_astrotext(self):
        self.text = str(f"{Globals.astro_count}/{Globals.threshold}")
        self.update_text()
