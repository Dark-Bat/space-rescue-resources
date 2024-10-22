from GameFrame import RoomObject, Globals
import random

class Asteroid(RoomObject):
    #class for Zorks weaponary

    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        #set image
        image = self.load_image("asteroid.png")
        self.set_image(image,50,49)
        #set travel direction
        angle = random.randint(135,225)
        self.set_direction(angle,10)
    
    def keep_in_room(self):
        if self.y < 0:
            self.y = 1
            self.y *=-1
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y = Globals.SCREEN_HEIGHT - self.height +1
            self.y_speed *= -1
    
    def step(self):
        self.keep_in_room()