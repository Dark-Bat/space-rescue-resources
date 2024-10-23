from GameFrame import RoomObject, Globals

class Laser(RoomObject):
    #Creates lasers
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        #Create image
        image = self.load_image("Laser.png")
        self.set_image(image,33,9)
        #add movement to laser
        self.set_direction(0,20)
    
    def outside_of_room(self):
        if self.x > Globals.SCREEN_WIDTH:
            self.room.delete_object(self)

    def step(self):
        self.outside_of_room()
        