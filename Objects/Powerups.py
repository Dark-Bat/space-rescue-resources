from GameFrame import RoomObject, Globals
import random
import pygame
class Shield(RoomObject):

    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("Shield.png")
        self.set_image(image,50,50)
        self.set_direction(180,5)
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
            print("Shield aquired")
            self.set_timer(750, self.deactivate_shield)

    def deactivate_shield(self):
        Globals.active_shield = False
        print("Shield Deactivated")

class RepairKit(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self,room, x, y)
        image = self.load_image("Repair_kit.png")
        self.set_image(image, 42, 42)



    