import pygame

class Globals:

    running = True
    FRAMES_PER_SECOND = 30

    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800

    SCORE = 0

    # - Set the starting number of lives - #
    LIVES = 3

    # - Set the Window display name - #
    window_name = 'Space Rescue'

    # - Set the order of the rooms - #
    levels = ["WelcomeScreen", "Difficulty_Selection", "ShipSelection", "GamePlay", "End_Room"]

    # - Set the starting level - #
    start_level = 0

    # - Set this number to the level you want to jump to when the game ends - #
    end_game_level = 4

    # - This variable keeps track of the room that will follow the current room - #
    # - Change this value to move through rooms in a non-sequential manner - #
    next_level = 0

    # - Change variable to True to exit the program - #
    exiting = False

    


# ############################################################# #
# ###### User Defined Global Variables below this line ######## #
# ############################################################# #

    total_count = 0
    destroyed_count = 0
    active_shield = False
    difficulty = 0
    astro_count = 0
    threshold = 5
    ship_type = ""  
    Swerver_Buff_Active = False
    Attractor_Buff_Active = False

    x_player = 0
    y_player = 0
    x_astro = 0
    y_astro = 0
    x_dif = 0
    y_dif = 0
    new_astronaut_angle = 0
