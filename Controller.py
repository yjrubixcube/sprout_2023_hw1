from typing import List
import pygame as pg
from Config import *
from Model import *
from operator import add
import random


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


def generate_food(foods: List[Food], walls: List[Wall], pos=None):
    # generate_origin = (100, 100)
    if pos == None:
        while 1:
            generate_origin = (
                SNAKE_SIZE * random.randint(0, SCREEN_WIDTH / SNAKE_SIZE),
                SNAKE_SIZE * random.randint(0, SCREEN_HEIGHT / SNAKE_SIZE),
            )

            for wall in walls:
                if (
                    wall.pos_x == generate_origin[0]
                    and wall.pos_y == generate_origin[1]
                ):
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
