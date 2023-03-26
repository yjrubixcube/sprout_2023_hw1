from typing import List
from Config import *
import pygame as pg
from operator import add


class Food:
    '''
    食物物件，初始化方法為 Food((左上角x, 左上角y))
    '''
    def __init__(self, pos):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.surf.fill(FOOD_COLOR)
        self.rect = self.surf.get_rect(topleft=pos)

    @property
    def pos_x(self):
        return self.rect.topleft[0]

    @property
    def pos_y(self):
        return self.rect.topleft[1]

class Poison:
    '''
    毒藥物件，初始化方法為 Poison((左上角x, 左上角y))
    '''
    def __init__(self, pos):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.surf.fill(POISON_COLOR)
        self.rect = self.surf.get_rect(topleft=pos)

    @property
    def pos_x(self):
        return self.rect.topleft[0]

    @property
    def pos_y(self):
        return self.rect.topleft[1]

class Wall:
    '''
    牆壁物件，初始化方法為 Wall((左上角x, 左上角y))
    '''
    def __init__(self, pos):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.surf.fill(WALL_COLOR)
        self.rect = self.surf.get_rect(topleft=pos)

    @property
    def pos_x(self):
        return self.rect.topleft[0]

    @property
    def pos_y(self):
        return self.rect.topleft[1]


class Player:
    '''
    玩家物件
    snake_list 紀錄每一段蛇的座標 (左上x, 左上y, 大小, 大小)
    '''
    def __init__(self):
        self.snake_list = [[200, 100, SNAKE_SIZE, SNAKE_SIZE]]
        

    @property
    def head_x(self):
        return self.snake_list[0][0]

    @property
    def head_y(self):
        return self.snake_list[0][1]

    @property
    def length(self):
        return len(self.snake_list)

    # 以下為大作業

    def new_block(self, new_pos):
        '''
        將新一段的資訊加到 snake_list 最後面
        '''
        # self.snake_list.insert(0, [*new_pos, SNAKE_SIZE, SNAKE_SIZE])
        # TODO
        self.snake_list.append([*new_pos, SNAKE_SIZE, SNAKE_SIZE])

    def draw_snake(self, screen):
        '''
        畫出蛇，顏色要黃藍相間，無回傳值
        顏色可以用 SNAKE_COLOR_YELLOW, SNAKE_COLOR_BLUE
        可以用 pg.draw.rect(screen, 顏色, (座標x, 座標y, 大小, 大小))
        '''
        # TODO
        col = True
        for block in self.snake_list:
            print(block)
            if col == True:
                pg.draw.rect(screen, SNAKE_COLOR_YELLOW, block)
            else:
                pg.draw.rect(screen, SNAKE_COLOR_BLUE, block)
            col = not col

    def check_border(self):
        '''
        判斷蛇的頭有沒有超出螢幕範圍
        有超出就回傳 True
        沒有超出回傳 False
        '''
        # TODO
        if (
            self.head_x < 0
            or self.head_x > SCREEN_WIDTH - SNAKE_SIZE
            or self.head_y < 0
            or self.head_y > SCREEN_HEIGHT - SNAKE_SIZE
        ):
            return True
        return False

    def move(self, direction):
        '''
        根據 direction 移動蛇的座標，無回傳值
        direction 為哪個按鍵被按到
        -1: 其他
        0: 上
        1: 右
        2: 下
        3: 左
        '''
        # TODO
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

        first_block = self.snake_list[0]
        last_block = self.snake_list.pop()
        last_block = list(map(add, first_block, movement))
        self.snake_list.insert(0, [*last_block, SNAKE_SIZE, SNAKE_SIZE])
    
    def detect_player_collision(self):
        '''
        判斷蛇的頭是否碰到蛇的其他段
        有碰到就回傳 True
        沒有碰到回傳 False
        '''
        # TODO
        first_block = [
            self.head_x,
            self.head_y,
            SNAKE_SIZE,
            SNAKE_SIZE,
        ]

        for block in self.snake_list[1:]:
            if block[:2] == first_block[:2]:
                return True

        else:
            return False

    def detect_wall_collision(self, walls: List[Wall]):
        '''
        判斷蛇的頭是否碰到牆壁
        有碰到就回傳 True
        沒有碰到回傳 False
        '''
        # TODO
        hx, hy = self.head_x, self.head_y

        for wall in walls:
            if (
                abs(hx - wall.rect.topleft[0]) < SNAKE_SIZE
                and abs(hy - wall.rect.topleft[1]) < SNAKE_SIZE
            ):
                return True

        return False

    def detect_food_collision(self, foods: List[Food]):
        '''
        判斷蛇的頭是否碰到食物
        有碰到就回傳 True
        沒有碰到回傳 False
        '''
        # TODO
        hx, hy = self.head_x, self.head_y

        for food in foods:
            if (
                abs(hx - food.rect.topleft[0]) < SNAKE_SIZE
                and abs(hy - food.rect.topleft[1]) < SNAKE_SIZE
            ):

                return True

        return False
    
    def detect_poison_collision(self, poison: Poison):
        '''
        判斷蛇的頭是否碰到毒藥
        有碰到就回傳 True
        沒有碰到回傳 False
        '''
        # TODO
        hx, hy = self.head_x, self.head_y
        if (
            abs(hx - poison.rect.topleft[0]) < SNAKE_SIZE
            and abs(hy - poison.rect.topleft[1]) < SNAKE_SIZE
        ):
            return True

        return False