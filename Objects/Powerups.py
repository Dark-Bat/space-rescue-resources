from GameFrame import RoomObject, Globals
from Hud import Lives
import random
import pygame
class Shield(RoomObject):
    #A class for the shield object
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("Shield.png")
        self.set_image(image,50,50)
        self.set_direction(180,10)
        self.register_collision_object("Ship")

    def step(self):
        self.outside_of_room()

    def outside_of_room(self):
        if self.x < 0:
            self.room.delete_object(self)

    def handle_collision(self, other, other_type):
        if other_type == "Ship":
            Globals.active_shield = True
            self.room.delete_object(self)
            self.set_timer(50, self.deactivate_shield)

    def deactivate_shield(self):
        #Required for the set_timer() function, unefficient tho :(
        Globals.active_shield = False

class RepairKit(RoomObject):
    def __init__(self, room, x, y):
        #Class for the repair kit powerup that restores a heart up to 3
        RoomObject.__init__(self,room, x, y)
        image = self.load_image("Repair_kit.png")
        self.set_image(image, 42, 42)
        self.set_direction(180,5)
        self.register_collision_object("Ship")

    def step(self):
        self.outside_of_room()

    def outside_of_room(self):
        if self.x < 0:
            self.room.delete_object(self)
    def handle_collision(self, other, other_type):
        #Only gives player a life if they have less than 3.
        if other_type == "Ship":
            if Globals.LIVES <3:
                Globals.LIVES += 1
                self.room.lives.update_image()
                print (Globals.LIVES)
            self.room.delete_object(self)

class ExtraHeart(RoomObject):
    # A class for giving the player an extra heart, has similar function to repair kit but can go to a higher amount of total hearts
    def __init__(self, room, x, y):
        RoomObject.__init__(self,room, x, y)
        image = self.load_image("Lives_frames/Lives_1.png")
        #Sets image for the object
        self.set_image(image, 125,23)
        self.set_direction(180,20)
        self.register_collision_object("Ship")

    def step(self):
        #Functions performed every game tick
        self.outside_of_room()

    def outside_of_room(self):
        if self.x < 0:
            self.room.delete_object(self)
    def handle_collision(self, other, other_type):
        #Handles collisions with other objects
        if other_type == "Ship":
            Globals.LIVES += 1
            self.room.lives.update_image()
            print (Globals.LIVES)
            self.room.delete_object(self)




    