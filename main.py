import pygame as pg
from Config import *
from Model import *
from Controller import *
import random
import time

from typing import List


def generate_food(foods: List[Food]):
    generate_origin = (100, 100)
    foods.append(Food(generate_origin))


def generate_wall(walls: List[Wall]):
    generate_origin = (200, 100)
    walls.append(Wall(generate_origin))


def show_snake_length():
    pass


"""
Initialize and Global variables
"""

pg.init()
pg.display.set_caption("Snakes!")

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

snake_length = 0

player = Player()

foods = []
walls = []

direction = 0

pg.time.set_timer(MOVE_EVENT, TIME_INTERVAL_MAX)

running = True

"""
Game Loop
"""

while running:

    if len(foods) == 0:
        generate_food(foods)

    if len(walls) == 0:
        generate_wall(walls)

    events = pg.event.get()
    pressed_keys = []
    for event in events:
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

        elif event.type == pg.KEYDOWN:
            pressed_keys.append(event.key)

    if check_border(player):
        break

    # print(True in pressed_keys)
    # # input()
    # time.sleep(1)

    # print(player_move(player, pressed_keys))
    input_result = player_key_input(player, pressed_keys)
    if input_result == "new":
        old = player.snake_list[0]
        player.new_block((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    print(input_result)
    direction = direction if input_result == None else input_result
    player_move(player, direction)

    # snake_length = detect_food_collision(snake_length, player, foods)
    # if detect_food_collision(1, player, foods): break
    # if game_over(player, walls):
    #     running = False

    screen.fill(BACKGROUND_COLOR)
    print(player.snake_list)
    for block in player.snake_list:
        # screen.blit(block.surf, block.rect)
        # screen.blit(block[0], block[1])
        # print(block)
        # print(pg.Rect(block))
        # screen.blit(pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE)), pg.Rect(block))
        pg.draw.rect(screen, rect=block, color=SNAKE_COLOR)
    # time.sleep(1)
    for food in foods:
        screen.blit(food.surf, food.rect)

    for wall in walls:
        screen.blit(wall.surf, wall.rect)

    pg.display.flip()

    clock.tick(40)
