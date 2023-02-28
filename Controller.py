from typing import List, Tuple, Sequence
import pygame as pg
from Config import *
from Model import *

def player_move(player: List[Player], pressed_keys: List):

    movement = (0, 0)

    for key in pressed_keys:
        if key == pg.K_UP:
            movement = (0, -SNAKE_SIZE)
            break
        if key == pg.K_DOWN:
            movement = (0, SNAKE_SIZE)
            break
        if key == pg.K_LEFT:
            movement = (-SNAKE_SIZE, 0)
            break
        if key == pg.K_RIGHT:
            movement = (SNAKE_SIZE, 0)
            break

    player[0].rect.move_ip(movement)

    return movement

def detect_food_collision(snake_length, player: List[Player], foods: List[Food]):

    for block in player:
        for food in foods:
            if abs(block.rect.centerx - food.rect.centerx) < SNAKE_SIZE \
                and abs(block.rect.centery - food.rect.centery) < SNAKE_SIZE:
                
                return True
            
    return False