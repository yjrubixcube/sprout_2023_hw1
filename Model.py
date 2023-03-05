from Config import *
import pygame as pg


class Player:
    def __init__(self):
        # self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        # self.surf.fill(SNAKE_COLOR)
        # self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.snake_list = []
        self.new_block((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.new_block((SCREEN_WIDTH / 2 + SNAKE_SIZE, SCREEN_HEIGHT / 2))
        self.new_block((SCREEN_WIDTH / 2 + SNAKE_SIZE, SCREEN_HEIGHT / 2 + SNAKE_SIZE))
        self.new_block((SCREEN_WIDTH / 2 + SNAKE_SIZE, 2 * SCREEN_HEIGHT / 2))
        # self.length = len(self.pos)
        # self.snake_list = [[self.surf, self.rect]]
        # self.snake_list.append
        print("first", self.snake_list)

    def new_block(self, new_pos):
        self.snake_list.append([*new_pos, SNAKE_SIZE, SNAKE_SIZE])

    def draw_snake(self, screen):
        for block in self.snake_list:
            pg.draw.rect(screen, SNAKE_COLOR, block)

    @property
    def head_x(self):
        print(self.snake_list[0][0])
        return self.snake_list[0][0]

    @property
    def head_y(self):
        print(self.snake_list[0][1])
        return self.snake_list[0][1]


class Food:
    def __init__(self, pos):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.surf.fill(FOOD_COLOR)
        self.rect = self.surf.get_rect(center=pos)


class Wall:
    def __init__(self, pos):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.surf.fill(WALL_COLOR)
        self.rect = self.surf.get_rect(center=pos)
