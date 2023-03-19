from typing import List
import pygame as pg
from Config import *
from Model import *
from operator import add
import random


def check_border(player: Player):
    if (
        player.head_x < 0
        or player.head_x > SCREEN_WIDTH
        or player.head_y < 0
        or player.head_y > SCREEN_HEIGHT
    ):
        return True
    return False


def key_input(pressed_keys: List):

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
    first_block = player.snake_list[0]
    last_block = player.snake_list.pop()
    # new_block = [first_block[0], pg.Rect()]
    last_block = list(map(add, first_block, movement))
    player.new_block(last_block)

    # return movement


def detect_wall_collision(player: Player, walls: List[Wall], direction):

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
    block = player.snake_list[0]  # [topleftx, toplefty, snakesize, snakesize]
    hx, hy = player.head_x + movement[0], player.head_y + movement[1]

    # block = list(map(add, block, movement))
    for wall in walls:
        # if abs(block[0] - wall.rect.topleft[0]) < SNAKE_SIZE \
        #     and abs(block[1] - wall.rect.topleft[1]) < SNAKE_SIZE:
        if (abs(hx - wall.rect.topleft[0]) < SNAKE_SIZE and abs(hy - wall.rect.topleft[1]) < SNAKE_SIZE):
            return True

    return False


def detect_food_collision(player: Player, foods: List[Food], direction):

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
    block = player.snake_list[0]  # [topleftx, toplefty, snakesize, snakesize]

    # block = list(map(add, block, movement))
    hx, hy = player.head_x + movement[0], player.head_y + movement[1]

    for food in foods:
        if (abs(hx - food.rect.topleft[0]) < SNAKE_SIZE and abs(hy - food.rect.topleft[1]) < SNAKE_SIZE):

            return True

    return False


def detect_player_collision(player: Player, direction):

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
        player.head_x + movement[0],
        player.head_y + movement[1],
        SNAKE_SIZE,
        SNAKE_SIZE,
    ]

    for block in player.snake_list[1:]:
        if block[:2] == first_block[:2]:
            return True

    else:
        return False
    
def generate_food(foods: List[Food], walls: List[Wall], pos=None):
    # generate_origin = (100, 100)
    if pos == None:
        while 1:
            generate_origin = (
                SNAKE_SIZE * random.randint(0, SCREEN_WIDTH/SNAKE_SIZE),
                SNAKE_SIZE * random.randint(0, SCREEN_HEIGHT/SNAKE_SIZE),
            )

            for wall in walls:
                if wall.pos_x == generate_origin[0] and wall.pos_y == generate_origin[1]:
                    break
            else:
                foods.append(Food(generate_origin))
                break
    else:
        generate_origin = pos
        foods.append(Food(generate_origin))

def generate_wall(walls: List[Wall], next_walls: List[Wall], pos=None):
    # generate_origin = (200, 100)

    if pos == None:
        # while 1:
        chosen = random.choice(next_walls)
        next_walls.remove(chosen)
        # new_wall = Wall((chosen.pos_x, chosen.pos_y))
        walls.append(chosen)

        add_next_wall = [
                Wall((chosen.pos_x, chosen.pos_y - SNAKE_SIZE)),
                Wall((chosen.pos_x, chosen.pos_y + SNAKE_SIZE)),
                Wall((chosen.pos_x - SNAKE_SIZE, chosen.pos_y)),
                Wall((chosen.pos_x + SNAKE_SIZE, chosen.pos_y)),
                 ]
        for wall in walls:
            for next in add_next_wall:
                if wall.pos_x == next.pos_x and wall.pos_y == next.pos_y:
                    add_next_wall.remove(next)
                    break
        
        next_walls.extend(add_next_wall)



    else:
        # generate_origin = pos
        walls.append(Wall(pos))
        if len(next_walls) == 0:
            next_walls.extend(
                [
                Wall((pos[0], pos[1] - SNAKE_SIZE)),
                Wall((pos[0], pos[1] + SNAKE_SIZE)),
                Wall((pos[0] - SNAKE_SIZE, pos[1])),
                Wall((pos[0] + SNAKE_SIZE, pos[1])),
                 ]
            )
