from typing import List
import pygame as pg
from Config import *
from Model import *
from operator import add
import random


def key_input(pressed_keys: List):
    '''
    從 pygame 的鍵盤輸入判斷哪些按鍵被按下
    回傳方向
    '''
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

# 以下為大作業

def generate_wall(walls: List[Wall], next_walls: List[Wall], player: Player, pos=None):
    '''
    生成一個 Wall 的物件並加到 walls 裡面，不能與現有牆壁或玩家重疊，新牆壁一定要與現有牆壁有接觸
    next_walls 紀錄下一次生牆壁時可以選用的座標
    無回傳值
    '''
    # TODO
    if len(walls) > 0:
        chosen = random.choice(next_walls)
        next_walls.remove(chosen)
        walls.append(chosen)

        add_next_wall = [
            Wall((chosen.pos_x, chosen.pos_y - SNAKE_SIZE)),
            Wall((chosen.pos_x, chosen.pos_y + SNAKE_SIZE)),
            Wall((chosen.pos_x - SNAKE_SIZE, chosen.pos_y)),
            Wall((chosen.pos_x + SNAKE_SIZE, chosen.pos_y)),
        ]
        for w in add_next_wall[:]:
            if (
                (w.pos_x < 0 or w.pos_x > SCREEN_WIDTH - SNAKE_SIZE)
                or (w.pos_y < 0 or w.pos_y > SCREEN_HEIGHT - SNAKE_SIZE)
                ):
                add_next_wall.remove(w)

        for next in add_next_wall[:]:
            for wall in walls:
                # if (
                #     (next.pos_x < 0 or next.pos_x > SCREEN_WIDTH - SNAKE_SIZE)
                #     or (next.pos_y < 0 or next.pos_y > SCREEN_HEIGHT - SNAKE_SIZE)
                #     ):
                #     add_next_wall.remove(next)
                for p in player.snake_list:
                    if (wall.pos_x == next.pos_x and wall.pos_y == next.pos_y) \
                        or (p[0] == next.pos_x and p[1] == next.pos_y):
                        add_next_wall.remove(next)
                        break
                else:
                    continue
                break
        next_walls.extend(add_next_wall)

    else:
        generate_origin = (
                SNAKE_SIZE * random.randint(0, SCREEN_WIDTH / SNAKE_SIZE - 1),
                SNAKE_SIZE * random.randint(0, SCREEN_HEIGHT / SNAKE_SIZE - 1),
            )
        pos = generate_origin
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
            for w in next_walls[:]:
                if (
                    (w.pos_x < 0 or w.pos_x > SCREEN_WIDTH - SNAKE_SIZE)
                    or (w.pos_y < 0 or w.pos_y > SCREEN_HEIGHT - SNAKE_SIZE)
                    ):
                    next_walls.remove(w)
    # print("nextwalls", len(next_walls))

def generate_food(foods: List[Food], walls: List[Wall], player: Player):
    
    '''
    在隨機位置生成一個Food的物件並加到foods裡面，不能與現有牆壁或玩家重疊
    無回傳值
    '''
    # TODO
    while 1:
        generate_origin = (
            SNAKE_SIZE * random.randint(0, SCREEN_WIDTH / SNAKE_SIZE - 1),
            SNAKE_SIZE * random.randint(0, SCREEN_HEIGHT / SNAKE_SIZE - 1),
        )

        for wall in walls:
            for p in player.snake_list:
                if (
                    wall.pos_x == generate_origin[0]
                    and wall.pos_y == generate_origin[1]
                ) or (
                    p[0] == generate_origin[0]
                    and p[1] == generate_origin[1]
                ):
                    break
            else:
                continue
            break
        else:
            foods.append(Food(generate_origin))
            break

def generate_poison(walls: List[Wall], foods: List[Food], player: Player):
    '''
    在隨機位置生成一個Poison的物件並回傳，不能與現有其他物件或玩家重疊
    無回傳值
    '''
    # TODO
    while 1:
        pos = (
                    SNAKE_SIZE * random.randint(0, SCREEN_WIDTH / SNAKE_SIZE - 1),
                    SNAKE_SIZE * random.randint(0, SCREEN_HEIGHT / SNAKE_SIZE - 1),
        )
        for wall in walls:
            for food in foods:
                for p in player.snake_list:
                    if (
                        (wall.pos_x == pos[0] and wall.pos_y == pos[1])
                        or (food.pos_x == pos[0] and food.pos_y == pos[1])
                        or (p[0] == pos[0] and p[0] == pos[1])
                    ):
                        break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            return Poison(pos)

def calculate_time_interval(player: Player):
    '''
    根據蛇的長度，計算並回傳每一秒有幾幀
    蛇的長度每增加4幀數就+1，從小到大，最大為 TIME_INTERVAL_MAX，最小為 TIME_INTERVAL_MIN
    '''
    l = player.length

    return min(TIME_INTERVAL_MIN + (l-1)//4, TIME_INTERVAL_MAX)