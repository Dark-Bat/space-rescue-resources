from GameFrame import RoomObject, Globals

class Powerups(RoomObject):

    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        #create image
        image = self.load_image("Sheild.png")
        self.set_image(image,46, 50)
        #add movement
        self.set_direction(180,20)
        #handle events
        self.register_collision_object("Ship")
    
    def outside_of_room(self):
        if self.x < 0:
            self.room.delete_object(self)

    def step(self):
        self.outside_of_room()

    