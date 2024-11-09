from GameFrame import RoomObject, Globals
from Hud import AstroText,AstroCollection

class Astronaut(RoomObject):

    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Astronaut.png")
        self.set_image(image,50,49)

        self.set_direction(180,5)

        self.register_collision_object("Ship")
        self.register_collision_object("Asteroid")

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