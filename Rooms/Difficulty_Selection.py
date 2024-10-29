from GameFrame import Level, Globals
from Objects.button import Button
import pygame

class Difficulty_Selection(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self,screen, joysticks)
        self.set_background_image("Background.png")

        self.handle_mouse_events = True

        self.easy_button = Button(self, 0, 0, "Shield.png", Globals.SCREEN_WIDTH//3, Globals.SCREEN_HEIGHT, self.easy)
        self.add_room_object(self.easy_button)

        self.medium_button = Button(self, Globals.SCREEN_WIDTH//3, 0, "Shield.png", Globals.SCREEN_WIDTH//3, Globals.SCREEN_HEIGHT, self.medium)
        self.add_room_object(self.medium_button)

        self.hard_button = Button(self, Globals.SCREEN_WIDTH//3*2, 0, "Shield.png", Globals.SCREEN_WIDTH//3, Globals.SCREEN_HEIGHT, self.hard)
        self.add_room_object(self.hard_button)

    def easy(self):
        print("easy mode selected")
        Globals.difficulty = 1
        self.running = False

    def medium(self):
        print("Medium mode selected")
        Globals.difficulty = 2
        self.running = False

    def hard(self):
        print("hard mode selected")
        Globals.difficulty = 3
        self.running = False




    

    