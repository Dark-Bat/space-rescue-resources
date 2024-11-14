from GameFrame import Level, Globals
from Objects.button import Button, Image

class ShipSelection(Level):
    #The room where the player chooses their ship type for the game. 
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        #Uses those handy buttons from earlier to 
        self.set_background_image = "Background.png"
        self.Attractor_Button = Button(self, 0, 0, "Attractor_frames\Rescue_0.png", 500, 500, self.Attractor)
        self.add_room_object(self.Attractor_Button)
        self.Swerver_Button = Button(self, Globals.SCREEN_WIDTH//2, 0, "Ship.png", 500, 500, self.Swerver)
        self.add_room_object(self.Swerver_Button)
        self.Ship_Selection_Image = Image(self, 0,0, "Ship_Selection_Screen.png", Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT)
        self.add_room_object(self.Ship_Selection_Image)
    
    def Attractor(self):
        Globals.ship_type = "Attractor"
        self.running = False
        
    def Swerver(self):
        Globals.ship_type = "Swerver"
        self.running = False