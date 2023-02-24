from Config import *
import pygame as pg

class Player:
    def __init__(self):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.length = 1

class Food:
    def __init__(self, pos):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.rect = self.surf.get_rect(center = pos)

class Wall:
    def __init__(self, pos):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.rect = self.surf.get_rect(center = pos)
