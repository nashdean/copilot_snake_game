"""
Manages the display and rendering.
"""

import random
import pygame
from game.colors import black, blue, red, white, green, dark_blue
from game.config import Easy, Medium, Hard, Insane


# Set display dimensions
dis_width = 800
dis_height = 600

# Create the display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by GitHub Copilot')

# Set the clock
clock = pygame.time.Clock()

# Font style
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def message(msg, color, y_offset=0, outline_color=black, outline_thickness=2):
    # Render the main message
    mesg = font_style.render(msg, True, color)
    
    # Render the outline
    for dx in range(-outline_thickness, outline_thickness + 1):
        for dy in range(-outline_thickness, outline_thickness + 1):
            if dx != 0 or dy != 0:
                outline_mesg = font_style.render(msg, True, outline_color)
                dis.blit(outline_mesg, [dis_width / 6 + dx, dis_height / 3 + y_offset + dy])
    
    # Render the main message on top of the outline
    dis.blit(mesg, [dis_width / 6, dis_height / 3 + y_offset])

def game_over_message():
    dis.fill(black)
    message("Game Over!", red, -50)
    message("Press R to Restart or Q to Quit", white, 50)
    pygame.display.update()

def start_menu():
    menu = True
    snake_block = 10
    snake_list = [[dis_width // 2, dis_height // 2]]
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(50, dis_height - snake_block) / 10.0) * 10.0  # Avoid banner area
    x1_change = 0
    y1_change = 0
    current_direction = None

    while menu:
        dis.fill(black)
        message("Snake Game", white, -100, outline_color=red, outline_thickness=2)
        message("Select Difficulty:", white,  outline_color=dark_blue, outline_thickness=1)
        message("- E-Easy", white, 50,  outline_color=dark_blue, outline_thickness=1)
        message("- M-Medium", white, 100,outline_color=dark_blue, outline_thickness=1)
        message("- H-Hard", white, 150,outline_color=dark_blue, outline_thickness=1)
        # message("- I-Insane", white, 200, outline_color=red, outline_thickness=1)

        # Draw the snake and food
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        for x in snake_list:
            pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

        pygame.display.update()
        pygame.time.delay(100)  # Delay to avoid key repetition

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    return Easy()
                elif event.key == pygame.K_m:
                    return Medium()
                elif event.key == pygame.K_h:
                    return Hard()
                elif event.key == pygame.K_i:
                    return Insane()

        # Move the snake towards the food
        if snake_list[0][0] < foodx:
            x1_change = snake_block
            y1_change = 0
            current_direction = "RIGHT"
        elif snake_list[0][0] > foodx:
            x1_change = -snake_block
            y1_change = 0
            current_direction = "LEFT"
        elif snake_list[0][1] < foody:
            y1_change = snake_block
            x1_change = 0
            current_direction = "DOWN"
        elif snake_list[0][1] > foody:
            y1_change = -snake_block
            x1_change = 0
            current_direction = "UP"

        # Update the snake's position
        new_head = [snake_list[0][0] + x1_change, snake_list[0][1] + y1_change]
        snake_list.insert(0, new_head)

        # Check if the snake has reached the food
        if snake_list[0][0] == foodx and snake_list[0][1] == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(50, dis_height - snake_block) / 10.0) * 10.0  # Avoid banner area
        else:
            snake_list.pop()