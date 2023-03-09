from typing import List, Tuple, Sequence
import pygame as pg
from Config import *
from Model import *
from operator import add
import random


def check_border(player: Player):
    if player.head_x < 0 or player.head_x > SCREEN_WIDTH or player.head_y < 0 or player.head_y > SCREEN_HEIGHT:
        return True
    return False


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
    elif direction == 2:  # down
        movement = (0, SNAKE_SIZE, 0, 0)
    elif direction == 3:  # left
        movement = (-SNAKE_SIZE, 0, 0, 0)
    elif direction == 1:  # right
        movement = (SNAKE_SIZE, 0, 0, 0)

    # player[0].rect.move_ip(movement)
    first_block = player.snake_list[0]
    last_block = player.snake_list.pop()
    # new_block = [first_block[0], pg.Rect()]
    last_block = list(map(add, first_block, movement))
    player.snake_list.insert(0, last_block)

    # return movement

def detect_wall_collision(player: Player, walls: List[Wall], direction):

    # for block in player.snake_list:
    if direction == -1: return
    if direction == 0: # up
        movement = (0, -SNAKE_SIZE, 0, 0)
    elif direction == 2:  # down
        movement = (0, SNAKE_SIZE, 0, 0)
    elif direction == 3:  # left
        movement = (-SNAKE_SIZE, 0, 0, 0)
    elif direction == 1:  # right
        movement = (SNAKE_SIZE, 0, 0, 0)
    block = player.snake_list[0] # [topleftx, toplefty, snakesize, snakesize]
    hx, hy = player.head_x + movement[0], player.head_y + movement[1]

    # block = list(map(add, block, movement))
    for wall in walls:
        # if abs(block[0] - wall.rect.topleft[0]) < SNAKE_SIZE \
        #     and abs(block[1] - wall.rect.topleft[1]) < SNAKE_SIZE:
        if abs(hx - wall.rect.topleft[0]) < SNAKE_SIZE \
            and abs(hy - wall.rect.topleft[1]) < SNAKE_SIZE:
            
            return True
            
    return False

def detect_food_collision(player: Player, foods: List[Food], direction):


    if direction == -1: return
    if direction == 0: # up
        movement = (0, -SNAKE_SIZE, 0, 0)
    elif direction == 2:  # down
        movement = (0, SNAKE_SIZE, 0, 0)
    elif direction == 3:  # left
        movement = (-SNAKE_SIZE, 0, 0, 0)
    elif direction == 1:  # right
        movement = (SNAKE_SIZE, 0, 0, 0)
    block = player.snake_list[0] # [topleftx, toplefty, snakesize, snakesize]

    # block = list(map(add, block, movement))
    hx, hy = player.head_x + movement[0], player.head_y + movement[1]


    for food in foods:
        if abs(hx - food.rect.topleft[0]) < SNAKE_SIZE \
            and abs(hy - food.rect.topleft[1]) < SNAKE_SIZE:
        # if abs(block[0] - food.rect.topleft[0]) < SNAKE_SIZE \
        #     and abs(block[1] - food.rect.topleft[1]) < SNAKE_SIZE:
            
            return True
            
    return False

def detect_player_collision(player: Player, direction):

    # first_block = player.snake_list[0]

    if direction == -1: return
    if direction == 0: # up
        movement = (0, -SNAKE_SIZE, 0, 0)
    elif direction == 2:  # down
        movement = (0, SNAKE_SIZE, 0, 0)
    elif direction == 3:  # left
        movement = (-SNAKE_SIZE, 0, 0, 0)
    elif direction == 1:  # right
        movement = (SNAKE_SIZE, 0, 0, 0)
    # first_block = player.snake_list[0] # [topleftx, toplefty, snakesize, snakesize]

    # first_block = list(map(add, first_block, movement))
    first_block = [player.head_x + movement[0], player.head_y + movement[1], SNAKE_SIZE, SNAKE_SIZE]

    for block in player.snake_list[1:]:
        if block[:2] == first_block[:2]:
            return True
        
    else:
        return False
    
def generate_food(foods: List[Food], pos):
    # generate_origin = (100, 100)
    generate_origin = pos
    foods.append(Food(generate_origin))

def generate_wall(walls: List[Wall], pos=None):
    # generate_origin = (200, 100)

    if pos == None:
        # while 1:
        chosen = random.choice(walls)
        wall_dir = random.randint(0, 3)

        if wall_dir == 0:
            new_wall = Wall((chosen.pos_x + SNAKE_SIZE, chosen.pos_y))
        elif wall_dir == 1:
            new_wall = Wall((chosen.pos_x - SNAKE_SIZE, chosen.pos_y))
        elif wall_dir == 2:
            new_wall = Wall((chosen.pos_x, chosen.pos_y + SNAKE_SIZE))
        elif wall_dir == 3:
            new_wall = Wall((chosen.pos_x, chosen.pos_y - SNAKE_SIZE))
        walls.append(new_wall)
    else:
        # generate_origin = pos
        walls.append(Wall(pos))
