from GameFrame import Level, Globals
from Objects.button import Button

import pygame

class Difficulty_Selection(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self,screen, joysticks)
        self.set_background_image("Background.png")

        self.handle_mouse_events = True

        #Creates three buttons that give a different difficulty depending on which one is clicked, uses the button.py file to easily do it. 
        self.easy_button = Button(self, 0, 0, "Diff_menu/easy_mode.png", Globals.SCREEN_WIDTH//3, Globals.SCREEN_HEIGHT, self.easy)
        self.add_room_object(self.easy_button)


        self.medium_button = Button(self, Globals.SCREEN_WIDTH//3, 0, "Diff_menu/medium_mode.png", Globals.SCREEN_WIDTH//3, Globals.SCREEN_HEIGHT, self.medium)
        self.add_room_object(self.medium_button)
        

        self.hard_button = Button(self, Globals.SCREEN_WIDTH//3*2, 0, "Diff_menu/hard_mode.png", Globals.SCREEN_WIDTH//3, Globals.SCREEN_HEIGHT, self.hard)
        self.add_room_object(self.hard_button)
        
    def easy(self):
        #the functions that run on differnt button click
        print("easy mode selected")
        Globals.difficulty = 1
        Globals.threshold = 5
        self.running = False

    def medium(self):
        print("Medium mode selected")
        Globals.difficulty = 2
        Globals.threshold = 10
        self.running = False

    def hard(self):
        print("hard mode selected")
        Globals.difficulty = 3
        Globals.threshold = 15
        self.running = False






    

    