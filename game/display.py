"""
Manages the display and rendering.
"""

import random
import pygame
from game.colors import black, blue, red, white, green, dark_blue, themes
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

# game/display.py

import pygame
from game.fonts import Text

class Slider:
    def __init__(self, x, y, width, height, options, primary_color, secondary_color, text_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.options = options
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.text_color = text_color
        self.selected_index = 0  # Initialize selected_index

    def handle_event(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(self.options)):
                option_x = self.x + i * (self.width // len(self.options))
                if option_x <= mouse_x <= option_x + (self.width // len(self.options)) and self.y <= mouse_y <= self.y + self.height:
                    self.selected_index = i

    def draw(self, surface):
        option_width = self.width // len(self.options)
        for i, option in enumerate(self.options):
            color = self.primary_color if i == self.selected_index else self.secondary_color
            option_x = self.x + i * option_width
            pygame.draw.rect(surface, color, [option_x, self.y, option_width, self.height])
            
            text = Text(option, 20, self.text_color)
            text_width, text_height = text.get_size()
            text_x = option_x + (option_width - text_width) // 2
            text_y = self.y + (self.height - text_height) // 2
            text.draw(surface, text_x, text_y)

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

# game/display.py

def animate_snake_menu(snake_block, snake_list, foodx, foody, x1_change, y1_change, current_direction, theme_colors):
    # Draw the snake and food with theme colors
    pygame.draw.rect(dis, theme_colors["food"], [foodx, foody, snake_block, snake_block])
    for x in snake_list:
        pygame.draw.rect(dis, theme_colors["snake"], [x[0], x[1], snake_block, snake_block])

    pygame.display.update()
    pygame.time.delay(100)  # Delay to avoid key repetition

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
        x1_change = 0
        y1_change = snake_block
        current_direction = "DOWN"
    elif snake_list[0][1] > foody:
        x1_change = 0
        y1_change = -snake_block
        current_direction = "UP"

    # Update the snake's position
    new_head = [snake_list[0][0] + x1_change, snake_list[0][1] + y1_change]
    snake_list.insert(0, new_head)

    # Check if the snake has reached the food
    if snake_list[0][0] == foodx and snake_list[0][1] == foody:
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(50, dis_height - snake_block) / 10.0) * 10.0
    else:
        snake_list.pop()  # Remove the last part of the snake if it hasn't eaten the food

    # Reset the snake if it grows too long
    if len(snake_list) > 70:
        snake_list = [[dis_width // 2, dis_height // 2]]

    return foodx, foody, x1_change, y1_change, current_direction, snake_list

def start_menu():
    menu = True
    theme_slider = Slider(100, 200, 600, 50, ["default", "light", "dark"], blue, white, black)
    difficulty_slider = Slider(100, 300, 600, 50, ["Classic", "Easy", "Medium", "Hard", "Insane"], blue, white, black)
    border_slider = Slider(100, 400, 600, 50, ["Yes", "No"], blue, white, black)
    
    # Initialize snake and food positions
    snake_block = 10
    snake_list = [[dis_width // 2, dis_height // 2]]
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(50, dis_height - snake_block) / 10.0) * 10.0
    x1_change = 0
    y1_change = 0
    current_direction = None

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False

            theme_slider.handle_event(event)
            difficulty_slider.handle_event(event)

        # Get the selected theme
        selected_theme = theme_slider.options[theme_slider.selected_index]
        theme_colors = themes[selected_theme]

        # Set the background color based on the selected theme
        dis.fill(theme_colors["background"])

        # Update the slider colors based on the selected theme
        theme_slider.primary_color = theme_colors["slider_primary"]
        theme_slider.secondary_color = theme_colors["slider_secondary"]
        theme_slider.text_color = theme_colors["text"]

        difficulty_slider.primary_color = theme_colors["slider_primary"]
        difficulty_slider.secondary_color = theme_colors["slider_secondary"]
        difficulty_slider.text_color = theme_colors["text"]

        # Draw the message and sliders with the theme colors
        message("Snake Game", theme_colors["snake"], -100, outline_color=theme_colors["food"], outline_thickness=2)
        theme_slider.draw(dis)
        difficulty_slider.draw(dis)

        # Animate the snake in the menu
        foodx, foody, x1_change, y1_change, current_direction, snake_list = animate_snake_menu(
            snake_block, snake_list, foodx, foody, x1_change, y1_change, current_direction, theme_colors
        )
        
        pygame.display.update()
        clock.tick(15)

    selected_theme = theme_slider.options[theme_slider.selected_index]
    selected_difficulty = difficulty_slider.options[difficulty_slider.selected_index]
    return selected_difficulty, selected_theme