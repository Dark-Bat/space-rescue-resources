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
        
        # sets image depending on which ship type you chose
        if Globals.ship_type == "Swerver":
            #Gains a mild speed buff while holding shift, but cant shield
            image = self.load_image("Rescue_invinc_frames/Rescue_0.png")
        else:
            #Can move astronauts towards player, but sacrifices movement speed
            image = self.load_image("Attractor_invinc_frames\Rescue_0.png")
        self.set_image(image,100,100)
        
        # register events
        self.handle_key_events = True
        self.handle_collision = True
        
        #Neccesary values for later
        self.can_shoot = True
        self.movement_buff = 1
        self.player_coords = (0,0)
        
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        #If shield is active, increase speed, and if either of the buffs are active act accordingly
        if Globals.active_shield == True:
            self.movement_buff = 2.5
        elif Globals.Swerver_Buff_Active == True:
            self.movement_buff = 1.5
        elif Globals.Attractor_Buff_Active == True:
            self.movement_buff = 0.1
        else:
            self.movement_buff = 1 

        #Simple 8 direction movement code, accounting for pythag theorum and movement increasing buffs
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
        if key[pygame.K_LSHIFT or pygame.K_RSHIFT]:
            #Reacts to shift key press
            if Globals.ship_type == "Attractor":
                #Sets a global boolean, that is used in other classes for functions and here for speed changes.
                Globals.Attractor_Buff_Active = True
            elif Globals.ship_type == "Swerver":
                Globals.Swerver_Buff_Active = True
                Globals.active_shield = False
        else:
            #Turns off the buffs if the player doesn't do anything
            Globals.Attractor_Buff_Active = False
            Globals.Swerver_Buff_Active = False
        if key[pygame.K_SPACE]:
            #Shoots a laser
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
            #function that shoots laser from ship
            new_laser = Laser(self.room, 
                            self.x + self.width, 
                            self.y + self.height/2 - 4)
            self.room.add_room_object(new_laser)
            self.can_shoot = False
            self.set_timer(10,self.reset_shot)
            self.room.shoot_laser.play()

    def reset_shot(self):
        #Neccesary for the set_timer() function
        self.can_shoot = True

    def update_sprite(self):
        #Changes the sprite of the boat during the game depending on what buffs are active, and what ship type was chosen.
        if Globals.active_shield == True and Globals.ship_type == "Swerver":
            image = self.load_image("Rescue_invinc_frames/Rescue_0.png")
        elif Globals.active_shield == True and Globals.ship_type == "Attractor":
            image = self.load_image("Attractor_invinc_frames\Rescue_0.png")
        elif Globals.ship_type == "Swerver":
            image = self.load_image("Ship.png")
        else:
            image = ("Images\Attractor_frames\Rescue_0.png")
        self.set_image(image,100,100)

