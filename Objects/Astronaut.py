from GameFrame import RoomObject

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
            self.room.score.update_score(50)
        if other_type == "Asteroid":
            self.room.delete_object(self)

    def outside_of_room(self):
        if self.x + self.width < -1:
            self.room.delete_object(self)