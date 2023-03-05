import pygame as pg
from Config import *
from Model import *
from Controller import *
import random
import time

from typing import List

def generate_food(foods: List[Food], pos):
    # generate_origin = (100, 100)
    generate_origin = pos
    foods.append(Food(generate_origin))

def generate_wall(walls: List[Wall], pos):
    # generate_origin = (200, 100)
    generate_origin = pos
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

direction = -1

pg.time.set_timer(MOVE_EVENT, TIME_INTERVAL_MAX)

running = True

"""
Game Loop
"""

while running:

    if len(foods) == 0:
        generate_food(foods, (100, 100))

    if len(walls) == 0:
        generate_wall(walls, (100, 200))

    events = pg.event.get()
    pressed_keys = []
    for event in events:
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        
        elif event.type == pg.KEYDOWN:
            pressed_keys.append(event.key)

            
    # print(True in pressed_keys)
    # # input()
    # time.sleep(1)
    
    # print(player_move(player, pressed_keys))
    input_result = player_key_input(player, pressed_keys)
    if input_result == 'new':
        old = player.snake_list[0]
        if direction == 0: # up
            new_block = (old[0], old[1] - SNAKE_SIZE)
        elif direction == 2: # down
            new_block = (old[0], old[1] + SNAKE_SIZE)
        elif direction == 3: # left
            new_block = (old[0] - SNAKE_SIZE, old[1])
        elif direction == 1: # right
            new_block = (old[0] + SNAKE_SIZE, old[1])
        player.new_block(new_block)
    print(input_result)
    direction = direction if input_result == None or input_result == "new" else input_result
    player_move(player, direction)
    
    # snake_length = detect_food_collision(snake_length, player, foods)
    if detect_wall_collision(player, walls): break
    if detect_food_collision(player, foods):
        player.new_block((foods[0].rect.topleft))
        foods.pop()
        generate_food(foods, (SNAKE_SIZE*random.randint(0, SCREEN_WIDTH/SNAKE_SIZE), SNAKE_SIZE*random.randint(0, SCREEN_HEIGHT/SNAKE_SIZE)))
    # if game_over(player, walls):
    #     running = False

    screen.fill(BACKGROUND_COLOR)
    # print(player.snake_list)
    for block in player.snake_list:
        # screen.blit(block.surf, block.rect)
        # screen.blit(block[0], block[1])
        # print(block)
        # print(pg.Rect(block))
        # screen.blit(pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE)), pg.Rect(block))
        # pg.draw.rect(screen, rect=pg.rect.Rect(), color=SNAKE_COLOR)
        pg.draw.rect(screen, rect=block, color=SNAKE_COLOR)
    # time.sleep(1)
    # print(pg.rect)
    for food in foods:
        screen.blit(food.surf, food.rect)

    for wall in walls:
        screen.blit(wall.surf, wall.rect)

    pg.display.flip()

    clock.tick(TIME_INTERVAL_MAX)