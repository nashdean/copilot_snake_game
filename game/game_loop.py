import pygame
import time
import random
from game.display import dis, clock, dis_width, dis_height, start_menu, message, game_over_message
from game.colors import black, red, blue, green, white, themes
from game.snake import our_snake
from game.fonts import display_score
from game.obstacles import generate_obstacles, draw_obstacles, generate_border_blocks, draw_border_blocks
from game.score import Score
from game.config import Classic, Easy, Medium, Hard, Insane



import random

def pause_game():
    paused = True
    message("Game Paused. Press P to Resume", white)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
        clock.tick(5)

def gameLoop():
    game_over = False
    game_close = False

    # Get the difficulty level from the start menu
    selected_difficulty, selected_theme = start_menu()

    # Initialize the difficulty
    if selected_difficulty == "Classic":
        difficulty = Classic()
    elif selected_difficulty == "Easy":
        difficulty = Easy()
    elif selected_difficulty == "Medium":
        difficulty = Medium()
    elif selected_difficulty == "Hard":
        difficulty = Hard()
    elif selected_difficulty == "Insane":
        difficulty = Insane()

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

    # Generate obstacles if not in Classic Mode
    if selected_difficulty != "Classic":
        border_blocks = generate_border_blocks(snake_block)
    else:
        border_blocks = []

    # Function to generate food position
    def generate_food():
        while True:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(50, dis_height - snake_block) / 10.0) * 10.0  # Avoid banner area
            if [foodx, foody] not in snake_list and (foodx, foody) not in obstacles and (foodx, foody) not in border_blocks:
                return foodx, foody

    # Generate obstacles based on the difficulty level
    obstacles = generate_obstacles(snake_block, snake_list, difficulty.num_obstacles)

    # Initialize food position using generate_food function
    foodx, foody = generate_food()

    # Get the initial high score for the current difficulty
    high_score = score_manager.get_high_score(difficulty.__class__.__name__)

    while not game_over:

        while game_close:
            game_over_message()
            display_score(length_of_snake - 1, high_score)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                    # Save the score if the game is over
                    score_manager.add_score(difficulty.__class__.__name__, length_of_snake - 1)

                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        # Save the score if the game is over
                        score_manager.add_score(difficulty.__class__.__name__, length_of_snake - 1)

                        pygame.quit()
                        quit()
                    if event.key == pygame.K_r:
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
                elif event.key == pygame.K_p:
                    pause_game()

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

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
        
        # Check for collisions with border blocks
        if (x1, y1) in border_blocks:
            game_close = True

        # Check for collisions with obstacles
        if (x1, y1) in obstacles:
            game_close = True

        if x1 == foodx and y1 == foody:
            length_of_snake += 1

            # Update the high score if the current score is higher
            if length_of_snake - 1 > high_score:
                high_score = length_of_snake - 1
                score_manager.add_score(difficulty.__class__.__name__, high_score)

            # Regenerate obstacles and add one new obstacle
            if len(obstacles) < 150 and selected_difficulty != "Classic":
                new_num_obstacles = min(len(obstacles) + 1, 150)
                new_obstacles = generate_obstacles(snake_block, snake_list, new_num_obstacles)
                if new_obstacles:
                    obstacles = new_obstacles

            # Speed up the snake as it gets longer in Classic Mode
            if selected_difficulty == "Classic":
                difficulty.speed += 0.3

            foodx, foody = generate_food()
            
        # Warp the snake to the other side of the screen in Classic Mode
        if difficulty.isBorder == False:
            if x1 >= dis_width:
                x1 = 0
            elif x1 < 0:
                x1 = dis_width - snake_block
            if y1 >= dis_height:
                y1 = 50  # Warp to just below the banner
            elif y1 < 50:
                y1 = dis_height - snake_block

        dis.fill(themes[selected_theme]["background"])
        pygame.draw.rect(dis, themes[selected_theme]["food"], [foodx, foody, snake_block, snake_block])
        our_snake(snake_block, snake_list, themes[selected_theme]["snake"])
        draw_obstacles(obstacles, snake_block, themes[selected_theme]["obstacle"])
        draw_border_blocks(border_blocks, snake_block, themes[selected_theme]["border"])

        display_score(length_of_snake - 1, high_score)
        pygame.display.update()

        clock.tick(difficulty.speed)

    # Save the score if the game is over
    score_manager.add_score(difficulty.__class__.__name__, length_of_snake - 1)

    pygame.quit()
    quit()