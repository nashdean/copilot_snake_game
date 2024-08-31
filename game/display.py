"""
Manages the display and rendering.
"""
import pygame
from game.colors import black, blue
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

def message(msg, color, y_offset=0):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3 + y_offset])

def start_menu():
    menu = True
    while menu:
        dis.fill(blue)
        message("Select Difficulty:", black)
        message("- E-Easy", black, 50)
        message("- M-Medium", black, 100)
        message("- H-Hard", black, 150)
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