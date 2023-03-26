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
    return

def generate_food(foods: List[Food], walls: List[Wall], player: Player):
    
    '''
    在隨機位置生成一個Food的物件並加到foods裡面，不能與現有牆壁或玩家重疊
    無回傳值
    '''
    # TODO
    return

def generate_poison(walls: List[Wall], foods: List[Food], player: Player):
    '''
    在隨機位置生成一個Poison的物件並回傳，不能與現有其他物件或玩家重疊
    '''
    # TODO
    return

def calculate_time_interval(player: Player):
    '''
    根據蛇的長度，計算並回傳每一秒有幾幀
    蛇的長度每增加4幀數就+1，從小到大，最大為 TIME_INTERVAL_MAX，最小為 TIME_INTERVAL_MIN
    '''
    # TODO
    return TIME_INTERVAL_MIN