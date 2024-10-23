from GameFrame import RoomObject, Globals
import pygame

class Ship(RoomObject):
    """
    A class for the player's avitar (the Ship)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Ship object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Ship.png")
        self.set_image(image,100,100)
        
        # register events
        self.handle_key_events = True
        
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        if key[pygame.K_w] and key[pygame.K_a]:
            self.y -= 7
            self.x -= 7
        elif key[pygame.K_w] and key[pygame.K_d]:
            self.y -= 7
            self.x += 7
        elif key[pygame.K_s] and key[pygame.K_a]:
            self.y += 7
            self.x -= 7
        elif key[pygame.K_s] and key[pygame.K_d]:
            self.y += 7
            self.x += 7
        elif key[pygame.K_w]:
            self.y -= 10
        elif key[pygame.K_s]:
            self.y += 10
        elif key[pygame.K_d]:
            self.x += 10
        elif key[pygame.K_a]:
            self.x -= 10

    def keep_in_room(self):
        #traps ship inside the box >:)
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
        elif self.x + self.height > Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - self.height
        elif self.x < 0:
            self.x = 0
    
    def step(self):
        #what happens to the boat every tick
        self.keep_in_room()
