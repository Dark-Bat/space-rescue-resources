from GameFrame import RoomObject, Globals
from Hud import AstroText
import math

class Astronaut(RoomObject):

    def __init__(self, room, x, y):
        #Creates astronaut objects, including image, direction and collision registration
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Astronaut.png")
        self.set_image(image,50,49)

        self.set_direction(180,5)

        self.register_collision_object("Ship")
        self.register_collision_object("Asteroid")
        
        #Defines variables for later functions
        self.refernce_x = 1
        self.reference_y = 1
        self.new_angle = 0
    def step(self):
        #Functions performed every game tick
        self.outside_of_room()


    def handle_collision(self, other, other_type):
        #Manages score, and win conditions of the game, as well as ship collisions
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
            #Code to remove the astronaut object if it gets hit by an asteroid
            self.room.delete_object(self)

    def outside_of_room(self):
        #Efficiency upgrade if astronaut leaves the screen
        if self.x + self.width < -1:
            self.room.delete_object(self)
        #
        if Globals.ship_type == "Attractor":
            if self.x + self.width > Globals.SCREEN_WIDTH:
                self.room.delete_object(self)
            elif self.y + self.width < -1:
                self.room.delete_object(self)
            elif self.y + self.width > Globals.SCREEN_HEIGHT:
                self.room.delete_object(self)
        #Getting position of player for attractor functions, put here for less clutter
        Globals.x_astro = self.x
        Globals.y_astro = self.y
        #Runs the attractor function here for less clutter in the step() function
        if Globals.Attractor_Buff_Active == True:
            self.Pathfind_player()
    
    def Pathfind_player(self):
        #Logic for the attractor function to draw astronaut object closer to ship. 
        ship_x = self.room.ship.x
        ship_y = self.room.ship.y
        #Finds the difference in the x and y position of the astronaut relative to the ship
        dif_x = ship_x - self.x
        dif_y = ship_y - self.y
        #Uses trig to find and set a new trajectory for the Astronaut.
        self.new_angle = (math.atan2(dif_y, dif_x) * 180 / math.pi) % 360
        self.set_direction(self.new_angle, 5)