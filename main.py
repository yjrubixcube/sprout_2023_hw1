import pygame as pg
from Config import *
from Model import *
from Controller import *

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

generate_wall(walls, next_walls, player)
generate_food(foods, walls, player)
poison = generate_poison(walls, foods, player)

direction = -1

time_interval = TIME_INTERVAL_MIN

pg.time.set_timer(MOVE_EVENT, TIME_INTERVAL_MIN)

"""
Game Loop
"""
running = True
while running:
    # 從 pygame 取得按鍵被按下的事件
    events = pg.event.get()
    pressed_keys = []
    for event in events:
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

        elif event.type == pg.KEYDOWN:
            pressed_keys.append(event.key)

    key = key_input(pressed_keys)
    pg.event.clear()
    direction = direction if key == None else key

    # 將蛇的最後一格存起來，長度變長的時候要加回去
    last_block = player.snake_list[-1]

    player.move(direction)

    # 各種物件碰撞判斷
    if player.check_border():
        print("hit border")
        break
    if player.detect_player_collision():
        print("hit self")
        break
    if player.detect_wall_collision(walls):
        print("hit wall")
        break
    if player.detect_food_collision(foods):
        player.new_block(last_block[:2])
        foods.pop()
        generate_wall(walls, next_walls, player)
        generate_food(foods, walls, player)
        poison = generate_poison(walls, foods, player)
    if player.detect_poison_collision(poison):
        player.snake_list.pop()
        print("poison")
        if player.length == 0:
            break
        poison = generate_poison(walls, foods, player)

    # 計算每秒的幀數 (fps)
    time_interval = calculate_time_interval(player)

    # 畫物件
    screen.fill(BACKGROUND_COLOR)
    player.draw_snake(screen)
    for food in foods:
        screen.blit(food.surf, food.rect)
    for wall in walls:
        screen.blit(wall.surf, wall.rect)
    screen.blit(poison.surf, poison.rect)

    # 把你的螢幕翻過來XD
    pg.display.flip()
    
    clock.tick(time_interval)

print(f"Your score is {player.length}")