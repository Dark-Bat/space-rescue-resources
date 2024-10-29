from GameFrame import TextObject, Globals, RoomObject
import pygame

class Button(RoomObject):
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

        

