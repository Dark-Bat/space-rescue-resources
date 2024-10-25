from GameFrame import RoomObject, Globals
from Objects.Hud import Score

class Laser(RoomObject):
    #Creates lasers
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        #Create image
        image = self.load_image("Laser.png")
        self.set_image(image,33,9)
        #add movement to laser
        self.set_direction(0,20)
        #Handle events
        self.register_collision_object("Asteroid")
        self.register_collision_object("Astronaut")
    
    def outside_of_room(self):
        if self.x > Globals.SCREEN_WIDTH:
            self.room.delete_object(self)

    def step(self):
        self.outside_of_room()
    
    #Event handlers
    def handle_collision(self,other, other_type):
        #handles laser collisions
        if other_type == "Asteroid":
            self.room.asteroid_shot.play()
            self.room.delete_object(other)
            self.room.score.update_score(5)
        elif other_type == "Astronaut":
            self.room.astronaut_shot.play()
            self.room.delete_object(other)
            self.room.score.update_score(-10)
        self.room.delete_object(self)
        