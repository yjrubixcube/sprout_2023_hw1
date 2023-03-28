from typing import List
import random
import pygame as pg
from Config import *
from Model import *


def key_input(pressed_keys: List):
    """
    從 pygame 的鍵盤輸入判斷哪些按鍵被按下
    回傳方向
    """
    for key in pressed_keys:
        if key == pg.K_UP:
            movement = UP
            break
        if key == pg.K_DOWN:
            movement = DOWN
            break
        if key == pg.K_LEFT:
            movement = LEFT
            break
        if key == pg.K_RIGHT:
            movement = RIGHT
            break
        if key == pg.K_a:
            return "new"
    else:
        return None
    return movement


# 以下為大作業


def generate_wall(walls: List[Wall], player: Player, direction: int):
    """
    生成一個 Wall 的物件並加到 walls 裡面，不能與現有牆壁或玩家重疊，新牆壁一定要與現有牆壁有接觸
    next_walls 紀錄下一次生牆壁時可以選用的座標
    無回傳值
    """
    # TODO
    if len(walls) > 0:
        new_pos_x = pos_x = walls[-1].pos_x
        new_pos_y = pos_y = walls[-1].pos_y
        cnt = 0
        while cnt < 100:
            cnt += 1
            if direction == UP:
                new_pos_x = pos_x
                new_pos_y = pos_y - SNAKE_SIZE
            elif direction == RIGHT:
                new_pos_x = pos_x + SNAKE_SIZE
                new_pos_y = pos_y
            elif direction == DOWN:
                new_pos_x = pos_x
                new_pos_y = pos_y + SNAKE_SIZE
            elif direction == LEFT:
                new_pos_x = pos_x - SNAKE_SIZE
                new_pos_y = pos_y
            print(f"trying wall: {new_pos_x}, {new_pos_y}")
            if new_pos_x < 0 or new_pos_x > SCREEN_WIDTH - SNAKE_SIZE:
                direction = random.choice([UP, DOWN])
                continue
            if new_pos_y < 0 or new_pos_y > SCREEN_HEIGHT - SNAKE_SIZE:
                direction = random.choice([RIGHT, LEFT])
                continue
            f = False
            for wall in walls:
                print(
                    f"wall: {wall.pos_x}, {wall.pos_y}, new: {new_pos_x}, {new_pos_y}"
                )
                if new_pos_x == wall.pos_x and new_pos_y == wall.pos_y:
                    direction = random.choice([d for d in DIRECTIONS if d != direction])
                    f = True
                    break
            if f:
                continue
            f = False
            for body in player.snake_list:
                if new_pos_x == body[0] and new_pos_y == body[1]:
                    direction = random.choice([d for d in DIRECTIONS if d != direction])
                    f = True
                    break
            if f:
                continue
            break
        walls.append(Wall((new_pos_x, new_pos_y)))
    else:
        generate_origin = (
            SNAKE_SIZE * random.randint(0, SCREEN_WIDTH / SNAKE_SIZE - 1),
            SNAKE_SIZE * random.randint(0, SCREEN_HEIGHT / SNAKE_SIZE - 1),
        )
        walls.append(Wall(generate_origin))
    return direction
    # print("nextwalls", len(next_walls))


def generate_food(foods: List[Food], walls: List[Wall], player: Player):

    """
    在隨機位置生成一個Food的物件並加到foods裡面，不能與現有牆壁或玩家重疊
    無回傳值
    """
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
                ) or (p[0] == generate_origin[0] and p[1] == generate_origin[1]):
                    break
            else:
                continue
            break
        else:
            foods.append(Food(generate_origin))
            break


def generate_poison(walls: List[Wall], foods: List[Food], player: Player):
    """
    在隨機位置生成一個Poison的物件並回傳，不能與現有其他物件或玩家重疊
    """
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
    """
    根據蛇的長度，計算並回傳每一秒有幾幀
    蛇的長度每增加4幀數就+1，從小到大，最大為 TIME_INTERVAL_MAX，最小為 TIME_INTERVAL_MIN
    """
    # TODO
    l = player.length

    return min(TIME_INTERVAL_MIN + (l - 1) // 4, TIME_INTERVAL_MAX)
