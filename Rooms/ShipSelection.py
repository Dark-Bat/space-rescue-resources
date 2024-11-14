from GameFrame import Level, Globals
from Objects.button import Button

class ShipSelection(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image = "Background.png"
        self.Attractor_Button = Button(self, 100, 100, "Attractor_frames\Rescue_0.png", 500, 500, self.Attractor)
        self.add_room_object(self.Attractor_Button)
        self.Swerver_Button = Button(self, 500, 100, "Ship.png", 500, 500, self.Swerver)
        self.add_room_object(self.Swerver_Button)
    
    def Attractor(self):
        Globals.ship_type = "Attractor"
        self.running = False
        
    def Swerver(self):
        Globals.ship_type = "Swerver"
        self.running = False