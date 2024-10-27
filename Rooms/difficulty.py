from GameFrame import Level, Globals

class Difficulty(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self,screen, joysticks)
        self.set_background_image("Background.png")
