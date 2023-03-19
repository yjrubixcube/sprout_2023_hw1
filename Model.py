from typing import List
from Config import *
import pygame as pg
from operator import add


class Food:
    def __init__(self, pos):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.surf.fill(FOOD_COLOR)
        self.rect = self.surf.get_rect(topleft=pos)

    @property
    def pos_x(self):
        return self.rect.topleft[0]

    @property
    def pos_y(self):
        return self.rect.topleft[1]


class Wall:
    def __init__(self, pos):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.surf.fill(WALL_COLOR)
        self.rect = self.surf.get_rect(topleft=pos)

    @property
    def pos_x(self):
        return self.rect.topleft[0]

    @property
    def pos_y(self):
        return self.rect.topleft[1]


class Player:
    def __init__(self):
        # self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        # self.surf.fill(SNAKE_COLOR)
        # self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        # self.snake_list = [
        #     [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SNAKE_SIZE, SNAKE_SIZE]
        # ]
        self.snake_list = [[200, 100, SNAKE_SIZE, SNAKE_SIZE]]
        

    def new_block(self, new_pos):
        self.snake_list.insert(0, [*new_pos, SNAKE_SIZE, SNAKE_SIZE])

    def draw_snake(self, screen):
        col = True
        for block in self.snake_list:
            print(block)
            if col == True:
                pg.draw.rect(screen, SNAKE_COLOR_YELLOW, block)
            else:
                pg.draw.rect(screen, SNAKE_COLOR_BLUE, block)
            col = not col

    def check_border(self):
        if (
            self.head_x < 0
            or self.head_x > SCREEN_WIDTH
            or self.head_y < 0
            or self.head_y > SCREEN_HEIGHT
        ):
            return True
        return False

    def move(self, direction):
        if direction == -1:
            return
        if direction == 0:  # up
            movement = (0, -SNAKE_SIZE)
        elif direction == 2:  # down
            movement = (0, SNAKE_SIZE)
        elif direction == 3:  # left
            movement = (-SNAKE_SIZE, 0)
        elif direction == 1:  # right
            movement = (SNAKE_SIZE, 0)

        # player[0].rect.move_ip(movement)
        first_block = self.snake_list[0]
        last_block = self.snake_list.pop()
        # new_block = [first_block[0], pg.Rect()]
        last_block = list(map(add, first_block, movement))
        self.new_block(last_block)

    def detect_wall_collision(self, walls: List[Wall], direction):
        # for block in player.snake_list:
        if direction == -1:
            return
        if direction == 0:  # up
            movement = (0, -SNAKE_SIZE)
        elif direction == 2:  # down
            movement = (0, SNAKE_SIZE)
        elif direction == 3:  # left
            movement = (-SNAKE_SIZE, 0)
        elif direction == 1:  # right
            movement = (SNAKE_SIZE, 0)
        block = self.snake_list[0]  # [topleftx, toplefty, snakesize, snakesize]
        hx, hy = self.head_x + movement[0], self.head_y + movement[1]

        # block = list(map(add, block, movement))
        for wall in walls:
            # if abs(block[0] - wall.rect.topleft[0]) < SNAKE_SIZE \
            #     and abs(block[1] - wall.rect.topleft[1]) < SNAKE_SIZE:
            if (
                abs(hx - wall.rect.topleft[0]) < SNAKE_SIZE
                and abs(hy - wall.rect.topleft[1]) < SNAKE_SIZE
            ):
                return True

        return False

    def detect_food_collision(self, foods: List[Food], direction):
        if direction == -1:
            return
        if direction == 0:  # up
            movement = (0, -SNAKE_SIZE)
        elif direction == 2:  # down
            movement = (0, SNAKE_SIZE)
        elif direction == 3:  # left
            movement = (-SNAKE_SIZE, 0)
        elif direction == 1:  # right
            movement = (SNAKE_SIZE, 0)
        block = self.snake_list[0]  # [topleftx, toplefty, snakesize, snakesize]

        # block = list(map(add, block, movement))
        hx, hy = self.head_x + movement[0], self.head_y + movement[1]

        for food in foods:
            if (
                abs(hx - food.rect.topleft[0]) < SNAKE_SIZE
                and abs(hy - food.rect.topleft[1]) < SNAKE_SIZE
            ):

                return True

        return False

    def detect_player_collision(self, direction):

        # first_block = player.snake_list[0]

        if direction == -1:
            return
        if direction == 0:  # up
            movement = (0, -SNAKE_SIZE)
        elif direction == 2:  # down
            movement = (0, SNAKE_SIZE)
        elif direction == 3:  # left
            movement = (-SNAKE_SIZE, 0)
        elif direction == 1:  # right
            movement = (SNAKE_SIZE, 0)
        # first_block = player.snake_list[0] # [topleftx, toplefty, snakesize, snakesize]

        # first_block = list(map(add, first_block, movement))
        first_block = [
            self.head_x + movement[0],
            self.head_y + movement[1],
            SNAKE_SIZE,
            SNAKE_SIZE,
        ]

        for block in self.snake_list[1:]:
            if block[:2] == first_block[:2]:
                return True

        else:
            return False

    @property
    def head_x(self):
        # print(self.snake_list[0][0])
        return self.snake_list[0][0]

    @property
    def head_y(self):
        # print(self.snake_list[0][1])
        return self.snake_list[0][1]

    @property
    def length(self):
        return len(self.snake_list)
