from GameFrame import RoomObject, Globals
from Powerups import Shield
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
        self.set_direction(angle, 7*Globals.difficulty)
        #register events
        self.register_collision_object("Ship")
    
    def keep_in_room(self):
        #Code that allows the asteroid to bounce between the walls
        if self.y < 0:
            self.y = 1
            self.y_speed *= -1
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y = Globals.SCREEN_HEIGHT - self.height +1
            self.y_speed *= -1
        elif self.x > Globals.SCREEN_WIDTH- self.width:
            self.x = Globals.SCREEN_WIDTH - self.width +1
            self.x_speed *= -1
        elif self.x < 0:
            self.x = 1
            self.x_speed *= -1
    
    def outside_of_room(self):
    #kills the asteroid if it leaves, for efficiency
        if self.x +self.width < 0 or self.y + self.height < 0:
            self.room.delete_object(self)
    
    def step(self):
        #Functions the code runs every game tick
        self.keep_in_room()
        self.outside_of_room()

    def handle_collision(self, other, other_type):
        #Manages the lives of the ship, and decides what happens on collision with the ship
        if other_type == "Ship":
            self.room.delete_object(self)
            if Globals.active_shield == False:
                self.room.asteroid_collision.play()
            else:
                self.room.asteroid_shot.play()
            if not Globals.active_shield:
                Globals.LIVES -= 1
            if Globals.LIVES > 0:
                self.room.lives.update_image()
            else:
                self.room.running = False
                Globals.LIVES = 3
