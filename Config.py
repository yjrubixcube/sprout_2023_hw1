import pygame as pg

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

BACKGROUND_COLOR = (0, 255, 0)
SNAKE_COLOR = (0, 0, 0)
FOOD_COLOR = (255, 0, 0)
WALL_COLOR = (127, 63, 0)

SNAKE_SIZE = 10

TEXT_COLOR = (0, 0, 0)

SCORE = 0

SNAKE_SPEED = 10
SNAKE_LENGTH = 1

TIME_INTERVAL_MIN = 5
TIME_INTERVAL_MAX = 10

MOVE_EVENT = pg.USEREVENT + 1 #custom event