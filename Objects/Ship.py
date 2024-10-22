from GameFrame import RoomObject
import pygame

class Ship(RoomObject):
    #Create the ship
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

    #Create image
        image = self.load_image("Ship.png")
        self.set_image(image,100,100)
    
    #Register events
        self.handle_key_events = True

    def key_pressed(self, key):
        #respond to up and down being pressed
        if key[pygame.K_w]:
            self.y_speed = -10
        elif key[pygame.K_s]:
            self.y_speed = 10