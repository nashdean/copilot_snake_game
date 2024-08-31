"""
Contains the snake-related functions and classes.
"""
import pygame
from game.display import dis
from game.colors import black

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])