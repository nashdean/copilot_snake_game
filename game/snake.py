"""
Contains the snake-related functions and classes.
"""
import pygame
from game.display import dis
from game.colors import themes

def our_snake(snake_block, snake_list, snake_color):
    for x in snake_list:
        pygame.draw.rect(dis, snake_color, [x[0], x[1], snake_block, snake_block])