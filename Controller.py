from typing import List, Tuple, Sequence
import pygame as pg
from Config import *
from Model import *
from operator import add

def player_key_input(player: Player, pressed_keys: List):

    movement = (0, 0, 0, 0)

    for key in pressed_keys:
        if key == pg.K_UP:
            movement = 0
            break
        if key == pg.K_DOWN:
            movement = 2
            break
        if key == pg.K_LEFT:
            movement = 3
            break
        if key == pg.K_RIGHT:
            movement = 1
            break
        if key == pg.K_a:
            return "new"
    else:
        return None
    return movement
    
def player_move(player: Player, direction):
    if direction == -1: return
    if direction == 0: # up
        movement = (0, -SNAKE_SIZE, 0, 0)
    elif direction == 2: # down
        movement = (0, SNAKE_SIZE, 0, 0)
    elif direction == 3: # left
        movement = (-SNAKE_SIZE, 0, 0, 0)
    elif direction == 1: # right
        movement = (SNAKE_SIZE, 0, 0, 0)

    # player[0].rect.move_ip(movement)
    first_block = player.snake_list[0]
    last_block = player.snake_list.pop()
    # new_block = [first_block[0], pg.Rect()]
    last_block = list(map(add, first_block, movement))
    player.snake_list.insert(0, last_block)

    # return movement

def detect_wall_collision(player: Player, walls: List[Wall]):

    # for block in player.snake_list:
    block = player.snake_list[0] # [topleftx, toplefty, snakesize, snakesize]
    for wall in walls:
        if abs(block[0] - wall.rect.topleft[0]) < SNAKE_SIZE \
            and abs(block[1] - wall.rect.topleft[1]) < SNAKE_SIZE:
            
            return True
            
    return False

def detect_food_collision(player: Player, foods: List[Food]):

    # for block in player.snake_list:
    block = player.snake_list[0] # [topleftx, toplefty, snakesize, snakesize]
    for food in foods:
        if abs(block[0] - food.rect.topleft[0]) < SNAKE_SIZE \
            and abs(block[1] - food.rect.topleft[1]) < SNAKE_SIZE:
            
            return True
            
    return False