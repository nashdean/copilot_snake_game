import pygame
import time
import random
from game.display import dis, clock, dis_width, dis_height, start_menu, message
from game.colors import black, red, blue, green
from game.snake import our_snake
from game.fonts import display_score
from game.obstacles import generate_obstacles, draw_obstacles
from game.score import Score


import random

def gameLoop():
    game_over = False
    game_close = False

    # Get the difficulty level from the start menu
    difficulty = start_menu()

    # Initialize the score manager
    score_manager = Score()

    # Define the banner height
    banner_height = 50
    
    # Initialize the snake's position and length
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_block = 10
    snake_list = []
    length_of_snake = 1
    # Initialize the current direction
    current_direction = None

    # Function to generate food position
    def generate_food():
        while True:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(50, dis_height - snake_block) / 10.0) * 10.0  # Avoid banner area
            if [foodx, foody] not in snake_list and (foodx, foody) not in obstacles:
                return foodx, foody

    # Generate obstacles based on the difficulty level
    obstacles = generate_obstacles(snake_block, snake_list, difficulty.num_obstacles)

    # Initialize food position using generate_food function
    foodx, foody = generate_food()

    # Get the initial high score for the current difficulty
    high_score = score_manager.get_high_score(difficulty.__class__.__name__)

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            display_score(length_of_snake - 1, high_score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and current_direction != "RIGHT":
                    x1_change = -snake_block
                    y1_change = 0
                    current_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and current_direction != "LEFT":
                    x1_change = snake_block
                    y1_change = 0
                    current_direction = "RIGHT"
                elif event.key == pygame.K_UP and current_direction != "DOWN":
                    y1_change = -snake_block
                    x1_change = 0
                    current_direction = "UP"
                elif event.key == pygame.K_DOWN and current_direction != "UP":
                    y1_change = snake_block
                    x1_change = 0
                    current_direction = "DOWN"

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # Draw the food
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        draw_obstacles(obstacles, snake_block)

        # Update the snake's position
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        
        # Check for collision with obstacles
        for obstacle in obstacles:
            if x1 == obstacle[0] and y1 == obstacle[1]:
                game_close = True
        
        # Check for collision with the banner
        if y1 < banner_height:
            game_close = True

        our_snake(snake_block, snake_list)
        display_score(length_of_snake - 1, high_score)


        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food()
            length_of_snake += 1

            # Update the high score if the current score is higher
            if length_of_snake - 1 > high_score:
                high_score = length_of_snake - 1
                score_manager.add_score(difficulty.__class__.__name__, high_score)

        clock.tick(difficulty.speed)

    # Save the score if the game is over
    score_manager.add_score(difficulty.__class__.__name__, length_of_snake - 1)

    pygame.quit()
    quit()