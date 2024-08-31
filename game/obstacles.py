"""
Handles obstacle creation and rendering.
"""
import random
import pygame
from game.display import dis, dis_width, dis_height
from game.colors import red

def generate_obstacles(snake_block, snake_list, num_obstacles):
    obstacles = []
    while len(obstacles) < num_obstacles:
        obstacle_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        obstacle_y = round(random.randrange(50, dis_height - snake_block) / 10.0) * 10.0  # Avoid banner area
        if [obstacle_x, obstacle_y] not in snake_list and (obstacle_x, obstacle_y) not in obstacles:
            obstacles.append((obstacle_x, obstacle_y))
    return obstacles

def draw_obstacles(obstacles, snake_block):
    for obstacle in obstacles:
        pygame.draw.rect(dis, red, [obstacle[0], obstacle[1], snake_block, snake_block])