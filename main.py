import pygame as pg
from Config import *
from Model import *
from Controller import *
import random

from typing import List


"""
Initialize and Global variables
"""

pg.init()
pg.display.set_caption("Snakes!")

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()


player = Player()

foods = []
walls = []
next_walls = []

direction = -1

time_interval = TIME_INTERVAL_MIN

pg.time.set_timer(MOVE_EVENT, TIME_INTERVAL_MAX)

running = True

"""
Game Loop
"""

while running:

    if len(foods) == 0:
        generate_food(foods, walls, (100, 100))

    if len(walls) == 0:
        generate_wall(walls, next_walls, (100, 200))

    events = pg.event.get()
    pressed_keys = []
    for event in events:
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

        elif event.type == pg.KEYDOWN:
            pressed_keys.append(event.key)

    if player.check_border():
        break

    # print(True in pressed_keys)
    # # input()
    # time.sleep(1)

    # print(player_move(player, pressed_keys))
    input_result = key_input(pressed_keys)
    if input_result == "new":
        old = player.snake_list[0]
        if direction == 0:  # up
            new_block = (old[0], old[1] - SNAKE_SIZE)
        elif direction == 2:  # down
            new_block = (old[0], old[1] + SNAKE_SIZE)
        elif direction == 3:  # left
            new_block = (old[0] - SNAKE_SIZE, old[1])
        else:  # right or not initialized
            new_block = (old[0] + SNAKE_SIZE, old[1])
        player.new_block(new_block)
    # print(input_result)
    direction = (
        direction if input_result == None or input_result == "new" else input_result
    )
    # player_move(player, direction)

    # snake_length = detect_food_collision(snake_length, player, foods)
    if player.detect_player_collision(direction):
        print("hit self")
        break
    if player.detect_wall_collision(walls, direction):
        print("hit wall")
        break
    if player.detect_food_collision(foods, direction):
        player.new_block((foods[0].rect.topleft))
        foods.pop()
        generate_food(foods, walls)
        print("hit food")
        generate_wall(walls, next_walls)
    # if game_over(player, walls):
    #     running = False
    if player.detect_player_collision(direction):
        print("hit self")
        break

    player.move(direction)

    time_interval = min(TIME_INTERVAL_MAX, time_interval + player.length // 4)

    screen.fill(BACKGROUND_COLOR)
    # print(player.snake_list)
    # for block in player.snake_list:
    #     # screen.blit(block.surf, block.rect)
    #     # screen.blit(block[0], block[1])
    #     # print(block)
    #     # print(pg.Rect(block))
    #     # screen.blit(pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE)), pg.Rect(block))
    #     # pg.draw.rect(screen, rect=pg.rect.Rect(), color=SNAKE_COLOR)
    #     print(block)
    #     pg.draw.rect(screen, rect=block, color=SNAKE_COLOR)
    player.draw_snake(screen)
    # time.sleep(1)
    # print(pg.rect)
    for food in foods:
        screen.blit(food.surf, food.rect)

    for wall in walls:
        screen.blit(wall.surf, wall.rect)

    pg.display.flip()

    # clock.tick(TIME_INTERVAL_MAX)
    clock.tick(time_interval)
