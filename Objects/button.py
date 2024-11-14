from GameFrame import Globals, RoomObject
import pygame

class Button(RoomObject):
    #This is a general purpose class, for whenever a button is needed, normally in starting rooms
    def __init__(self, room, x, y, image, width, height, function):
        RoomObject.__init__(self, room, x, y)
        self.pressed = False
        image = self.load_image(image)
        self.set_image(image, width, height)

        self.function = function

        self.handle_mouse_events = True

    def clicked(self, button_number):
        if button_number == 1:
            self.function()

class Image(RoomObject):
    #A class if an image is required to have no function, is grouped in button function for ease of use
    def __init__(self, room, x, y, image, width, height):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image(image)
        self.set_image(image, width, height)

        

