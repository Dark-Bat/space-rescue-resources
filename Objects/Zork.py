from GameFrame import RoomObject, Globals
from Objects.Asteroid import Asteroid
from Objects.Astronaut import Astronaut
import random

class Zork(RoomObject):
    #class that defines the zork 
    def __init__(self, room, x, y):
        #create the boss object
        RoomObject.__init__(self, room, x, y)
        #set the image
        image = self.load_image("Zork.png")
        self.set_image(image,135,165)
        #set movement
        self.y_speed = random.choice([-10,10])
        #start asteroid timer
        asteroid_spawn_time = random.randint(1,2)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)
        #start astronaut timer
        astronaut_spawn_time = random.randint(30, 200)
        self.set_timer(astronaut_spawn_time, self.spawn_astronaut)

    def keep_in_room(self):
        #traps zork inside his box
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *=-1

    def step(self):
        self.keep_in_room()
    
    def spawn_asteroid(self):
        #randomly spawns asteroid
        #spawn asteroid and add to room
        new_asteroid = Asteroid(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_asteroid)
        #reset time for next asteroid spawn
        asteroid_spawn_time = random.randint(15, 150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)

    def spawn_astronaut(self):
        """
        Randomly spawns a new astronaut
        """
        # spawn astronaut and add to room
        new_astronaut = Astronaut(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_astronaut)
        
        # reset timer for next astronaut spawn
        astronaut_spawn_time = random.randint(30, 200)
        self.set_timer(astronaut_spawn_time, self.spawn_astronaut)