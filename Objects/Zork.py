from GameFrame import RoomObject, Globals
import random

class Zork(RoomObject):
    #class that defines the zork 
    def __init__(self, room, x, y):
        #create the boss object
        RoomObject.__init__(self, room, x, y)
        #set the image
        image = self.load_image("Zork.png")
        self.set_image(image,135,165)
        #set movement
        self.y_speed = random.choice([-10,10])

    def keep_in_room(self):
        #traps zork inside his box
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *=-1

    def step(self):
        self.keep_in_room()