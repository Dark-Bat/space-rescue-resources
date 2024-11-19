from GameFrame import Level, Globals
from Objects.Title import Victory, Failure
from Objects.Title import Title
import pygame

class End_Room(Level):
    #The victory screen or loss screen depending on what score you got in the game
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")
        
        # add title object
        if Globals.astro_count == Globals.threshold:
            self.add_room_object(Victory(self, 240, 200))
        else:
            self.add_room_object(Failure(self, 240, 200))

        Globals.astro_count = 0
        Globals.SCORE = 0
        Globals.LIVES = 3
        Globals.active_shield = False