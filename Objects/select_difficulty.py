from GameFrame import RoomObject, TextObject, Globals
import pygame

class select_difficulty(TextObject):
    def __init__(self, room, x, y, text='Not Set', size=60, font='Comic Sans MS', colour=(255,255,255)):
        TextObject.__init__(room, x, y, text, size, font, colour)