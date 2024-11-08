from GameFrame import Level, Globals
from Objects.Title import Victory, Failure
from Objects.Title import Title
import pygame

class End_Room(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")
        
        # add title object
        if Globals.astro_count == Globals.threshold:
            self.add_room_object(Victory(self, 240, 200))
        else:
            self.add_room_object(Failure(self, 240, 200))
        
        #load sounds
        self.bg_music = self.load_sound("Music.mp3")

        #Play background music
        self.bg_music.play(loops=1)
        self.bg_music.set_volume(0.1)