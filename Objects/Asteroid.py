from GameFrame import RoomObject

class Asteroid(RoomObject):
    #class for Zorks weaponary

    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        #set image
        image = self.load_image("asteroid.png")
        self.set_image(image,50,49)