"""
Manages font styles and rendering messages.
"""
from game.display import dis, dis_width  # Add this import
import pygame
from game.colors import black  # Import the black color

# Font style
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

class Text:
    def __init__(self, text, font_size, color):
        self.text = text
        self.font_size = font_size
        self.color = color
        self.font = pygame.font.SysFont(None, font_size)
        self.rendered_text = self.font.render(text, True, color)

    def draw(self, surface, x, y):
        surface.blit(self.rendered_text, (x, y))

    def get_size(self):
        return self.font.size(self.text)
    
def display_score(score, high_score):
    banner_height = 50
    banner_color = (200, 200, 200)  # Light grey color for the banner
    pygame.draw.rect(dis, banner_color, [0, 0, dis_width, banner_height])
    
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [10, 10])  # Adjust position to fit within the banner

    high_score_value = score_font.render("Hi Score: " + str(high_score), True, (100, 100, 100))  # Grey color for high score
    dis.blit(high_score_value, [dis_width - 200, 10])  # Adjust position to fit within the banner

