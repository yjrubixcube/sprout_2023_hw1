from Config import *
import pygame as pg

class Player:
    def __init__(self):
        # self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        # self.surf.fill(SNAKE_COLOR)
        # self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.snake_list = [[SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SNAKE_SIZE, SNAKE_SIZE]]
        # self.snake_list = [[SCREEN_WIDTH/2 - SNAKE_SIZE/2, SCREEN_HEIGHT/2 - SNAKE_SIZE/2, SNAKE_SIZE, SNAKE_SIZE]]
        # self.snake_list.append([SCREEN_WIDTH/2 + SNAKE_SIZE, SCREEN_HEIGHT/2, SNAKE_SIZE, SNAKE_SIZE])
        # self.snake_list.append([SCREEN_WIDTH/2 + SNAKE_SIZE, SCREEN_HEIGHT/2 + SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE])
        # self.snake_list.append([SCREEN_WIDTH/2 + SNAKE_SIZE, SCREEN_HEIGHT/2 + 2*SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE])
        # self.length = len(self.pos)
        # self.snake_list = [[self.surf, self.rect]]
        # self.snake_list.append
        print("first", self.snake_list)

    def new_block(self, new_pos):
        self.snake_list.insert(0, [*new_pos, SNAKE_SIZE, SNAKE_SIZE])
    
    def draw_snake(self, screen):
        for block in self.snake_list:
            pg.draw.rect(screen, SNAKE_COLOR, block)

class Food:
    def __init__(self, pos):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.surf.fill(FOOD_COLOR)
        self.rect = self.surf.get_rect(topleft=pos)

class Wall:
    def __init__(self, pos):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.surf.fill(WALL_COLOR)
        self.rect = self.surf.get_rect(topleft = pos)
