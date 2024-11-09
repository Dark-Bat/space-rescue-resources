from GameFrame import RoomObject, Globals
from Objects.Laser import Laser
from Objects.Astronaut import Astronaut
import pygame
import math

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
        self.handle_collision = True
        self.ship_type = ""
        

        self.can_shoot = True
        self.movement_buff = 1
        
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if Globals.active_shield == True:
            self.movement_buff = 2.5
        else:
            self.movement_buff = 1

        if key[pygame.K_w] and key[pygame.K_a]:
            self.y -= 7*self.movement_buff
            self.x -= 7*self.movement_buff
        elif key[pygame.K_w] and key[pygame.K_d]:
            self.y -= 7*self.movement_buff
            self.x += 7*self.movement_buff
        elif key[pygame.K_s] and key[pygame.K_a]:
            self.y += 7*self.movement_buff
            self.x -= 7*self.movement_buff
        elif key[pygame.K_s] and key[pygame.K_d]:
            self.y += 7*self.movement_buff
            self.x += 7*self.movement_buff
        elif key[pygame.K_w]:
            self.y -= 10*self.movement_buff
        elif key[pygame.K_s]:
            self.y += 10*self.movement_buff
        elif key[pygame.K_d]:
            self.x += 10*self.movement_buff
        elif key[pygame.K_a]:
            self.x -= 10*self.movement_buff
        if key[pygame.K_LCTRL or pygame.K_RCTRL]:
            if self.ship_type == "Attractor":
                self.Attractor_Buff()
            elif self.ship_type == "Swerver":
                self.Swerver_Buff()
        if key[pygame.K_SPACE]:
            self.shoot_laser()

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

        Globals.x_player = self.x
        Globals.y_player = self.y
    
    def step(self):
        #what happens to the boat every tick
        self.keep_in_room()
        self.update_sprite()

    def shoot_laser(self):
        if self.can_shoot:
            #Shoots laser from ship
            new_laser = Laser(self.room, 
                            self.x + self.width, 
                            self.y + self.height/2 - 4)
            self.room.add_room_object(new_laser)
            self.can_shoot = False
            self.set_timer(10,self.reset_shot)
            self.room.shoot_laser.play()

    def reset_shot(self):
        self.can_shoot = True

    def update_sprite(self):
        if Globals.active_shield == True:
            image = self.load_image("Rescue_invinc_frames/Rescue_0.png")
        else:
            image = self.load_image("Ship.png")
        self.set_image(image,100,100)

    def Swerver_Buff(self):
        self.movement_buff = 1.25
        Globals.active_shield = False

    def Attractor_Buff(self):
        #Checks what quadrant the astronaut is in relative to the ship, and finds the distance between them
        if Globals.x_player < Globals.x_astro:
            Globals.x_dif = Globals.x_astro - Globals.x_player
            print(Globals.x_dif)
        elif Globals.x_player < Globals.x_astro:
            Globals.x_dif = Globals.x_player - Globals.x_astro 
            print(Globals.x_dif)
        if Globals.y_player < Globals.y_astro:
            Globals.y_dif = Globals.y_astro - Globals.y_player
            print(Globals.y_dif)
        elif Globals.y_player < Globals.y_astro:
            Globals.y_dif = Globals.y_player - Globals.y_astro
            print(Globals.y_dif)
        Globals.new_astronaut_angle = math.atan2(int(Globals.y_dif,Globals.x_dif))*180/math.pi