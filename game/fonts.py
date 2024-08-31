"""
Manages font styles and rendering messages.
"""
import pygame
from game.colors import black  # Import the black color
from game.display import dis, dis_width

# Font style
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def display_score(score, high_score):
    banner_height = 50
    banner_color = (200, 200, 200)  # Light grey color for the banner
    pygame.draw.rect(dis, banner_color, [0, 0, dis_width, banner_height])
    
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [10, 10])  # Adjust position to fit within the banner

    high_score_value = score_font.render("Hi Score: " + str(high_score), True, (100, 100, 100))  # Grey color for high score
    dis.blit(high_score_value, [dis_width - 200, 10])  # Adjust position to fit within the banner

