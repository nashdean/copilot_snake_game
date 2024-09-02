"""
Handles obstacle creation and rendering.
"""
import random
import pygame
from game.display import dis, dis_width, dis_height
from game.colors import red, dark_blue
def generate_border_blocks(snake_block):
    border_blocks = []

    # Top border
    for x in range(0, dis_width, snake_block):
        border_blocks.append((x, 50))  # 50 to avoid the banner area

    # Bottom border
    for x in range(0, dis_width, snake_block):
        border_blocks.append((x, dis_height - snake_block))

    # Left border
    for y in range(50, dis_height, snake_block):  # 50 to avoid the banner area
        border_blocks.append((0, y))

    # Right border
    for y in range(50, dis_height, snake_block):  # 50 to avoid the banner area
        border_blocks.append((dis_width - snake_block, y))

    return border_blocks

def draw_border_blocks(border_blocks, snake_block):
    for block in border_blocks:
        pygame.draw.rect(dis, dark_blue, [block[0], block[1], snake_block, snake_block])

def generate_obstacles(snake_block, snake_list, num_obstacles):
    obstacles = []
    while len(obstacles) < num_obstacles:
        obstacle_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        obstacle_y = round(random.randrange(50, dis_height - snake_block) / 10.0) * 10.0  # Avoid banner area

        # Check if the obstacle is within a 10-block radius of the snake
        too_close = False
        for segment in snake_list:
            if abs(obstacle_x - segment[0]) < 10 * snake_block and abs(obstacle_y - segment[1]) < 10 * snake_block:
                too_close = True
                break

        if not too_close and [obstacle_x, obstacle_y] not in snake_list and (obstacle_x, obstacle_y) not in obstacles:
            obstacles.append((obstacle_x, obstacle_y))
    return obstacles

def draw_obstacles(obstacles, snake_block):
    for obstacle in obstacles:
        pygame.draw.rect(dis, red, [obstacle[0], obstacle[1], snake_block, snake_block])