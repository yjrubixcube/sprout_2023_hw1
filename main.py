import pygame as pg
from Config import *
from Model import *
import random

from typing import List

def generate_food(foods: List[Food]):
    generate_origin = (100, 100)
    foods.append(Food(generate_origin))

def generate_wall(walls: List[Wall]):
    generate_origin = (100, 100)
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

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
            
    # pressed_keys = pg.key.get_pressed()

    # player_move(player.rect, pressed_keys)
    
    # snake_length = detect_food_collision(snake_length, player, foods)

    # if game_over(player, walls):
    #     running = False

    screen.fill(BACKGROUND_COLOR)
    screen.blit(player.surf, player.rect)

    for food in foods:
        screen.blit(food.surf, food.rect)

    for wall in walls:
        screen.blit(wall.surf, wall.rect)

    pg.display.flip()

    clock.tick(40)