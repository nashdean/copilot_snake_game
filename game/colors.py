"""
Defines color constants.
"""
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dark_blue = (0, 0, 139)

"""
Defines color constants and themes.
"""

# Default theme colors
default_background = (155,188,15)
default_snake = (8, 41, 85)
default_food = (255, 255, 0)
default_obstacle = (48,98,48)
default_border = (15,56,15)
default_text = (0, 0, 0)
default_slider_primary = (50, 153, 213)
default_slider_secondary = (200, 200, 200)

# Light theme colors
light_background = (255, 255, 255)
light_snake = (0, 0, 0)
light_food = (0, 255, 255)
light_obstacle = (128, 128, 128)
light_border = (0, 0, 139)
light_text = (0, 0, 0)
light_slider_primary = (200, 200, 200)
light_slider_secondary = (250, 240, 250)

# Dark theme colors
dark_background = (0, 0, 0)
dark_snake = (255, 255, 255)
dark_food = (0, 255, 0)
dark_obstacle = (255, 175, 175)
dark_border = (100, 0, 0)
dark_text = (255, 255, 255)
dark_slider_primary = (100, 100, 100)
dark_slider_secondary = (50, 50, 50)

# Define themes
themes = {
    "default": {
        "background": default_background,
        "snake": default_snake,
        "food": default_food,
        "obstacle": default_obstacle,
        "border": default_border,
        "text": default_text,
        "slider_primary": default_slider_primary,
        "slider_secondary": default_slider_secondary,
    },
    "light": {
        "background": light_background,
        "snake": light_snake,
        "food": light_food,
        "obstacle": light_obstacle,
        "border": light_border,
        "text": light_text,
        "slider_primary": light_slider_primary,
        "slider_secondary": light_slider_secondary,
    },
    "dark": {
        "background": dark_background,
        "snake": dark_snake,
        "food": dark_food,
        "obstacle": dark_obstacle,
        "border": dark_border,
        "text": dark_text,
        "slider_primary": dark_slider_primary,
        "slider_secondary": dark_slider_secondary,
    },
}