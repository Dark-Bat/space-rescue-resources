from GameFrame import RoomObject, Globals
from Hud import AstroText,AstroCollection
import math

class Astronaut(RoomObject):

    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Astronaut.png")
        self.set_image(image,50,49)

        self.set_direction(180,5)

        self.register_collision_object("Ship")
        self.register_collision_object("Asteroid")
        
        self.refernce_x = 1
        self.reference_y = 1
        self.new_angle = 0
    def step(self):
        self.outside_of_room()


    def handle_collision(self, other, other_type):
        if other_type == "Ship":
            self.room.delete_object(self)
            self.room.astronaut_saved.play()
            self.room.score.update_score(50)
            Globals.astro_count += 1
            print(Globals.astro_count)
            self.room.AstroText.update_astrotext()
            #win condition
            if Globals.astro_count == Globals.threshold:
                self.room.running = False

        if other_type == "Asteroid":
            self.room.delete_object(self)

    def outside_of_room(self):
        if self.x + self.width < -1:
            self.room.delete_object(self)
        #Getting position of player for attractor functions, put here for less clutter
        Globals.x_astro = self.x
        Globals.y_astro = self.y
        if Globals.Attractor_Buff_Active == True:
            self.Pathfind_player()
    
    def Pathfind_player(self):
        ship_x = self.room.ship.x
        ship_y = self.room.ship.y
        dif_x = ship_x - self.x
        dif_y = ship_y - self.y
        self.new_angle = (math.atan2(dif_y, dif_x) * 180 / math.pi) % 360
        self.set_direction(self.new_angle, 5)