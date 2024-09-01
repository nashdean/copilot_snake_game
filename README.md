# Snake Game

This is a classic Snake game implemented in Python using Pygame. The game was created entirely with the help of GitHub Copilot.

## How to Run the Game

### Prerequisites

- Python 3.9 or later
- Pygame
- PyYAML

### Running the Game

1. **Clone the repository**
```bash
git clone https://github.com/nashdean/copilot_snake_game.git
cd copilot_snake_game
```
2. **Install the dependencies**
```bash
pip install -r requirements.txt
```
3. **Run the game:**
```bash
python main.py
```

### Using Dev Containers
If you are using Visual Studio Code with Dev Containers, the development environment will be set up automatically. Just open the project in VS Code and select "Reopen in Container" when prompted.

# Game Rules
- The objective of the game is to eat as much food as possible without running into the walls or the snake's own body.
- The game ends if the snake collides with the walls or its own body.
- The snake grows longer each time it eats food.
- The game has different difficulty levels, each with a different speed and number of obstacles.

## How to Play
1. Start the game:
    - Run the game using the instructions above.
    - Select the difficulty level from the start menu.
2. Control the snake:
    - Use the arrow keys to control the direction of the snake.
    - The snake will move continuously in the direction of the last arrow key pressed.
3. Eat the food:
    - Guide the snake to the green food blocks to eat them.
    - Each time the snake eats food, it grows longer.
4. Avoid obstacles:
    - Avoid running into the red obstacles that appear on the screen.
5. Game over:
    - The game ends if the snake runs into the walls, its own body, or an obstacle.
    - Your score will be displayed, and the high score for the selected difficulty level will be updated if you achieved a new high score.
## High Scores
- The game keeps track of the highest scores for each difficulty level.
- High scores are stored in a high_scores.yaml file.
- The highest score for the current difficulty level is displayed on the score banner during the game.

# Development
This game was created entirely with the help of GitHub Copilot. Copilot assisted in writing the code, generating functions, and creating the overall structure of the game.

## Project Structure

```
.devcontainer/
    devcontainer.json
    Dockerfile
.gitignore
game/
    __init__.py
    __pycache__/
    colors.py
    config.py
    display.py
    fonts.py
    game_loop.py
    obstacles.py
    score.py
    snake.py
high_scores.yaml
main.py
requirements.txt
```

## Key Files
- main.py: Entry point of the application.
- game/game_loop.py: Contains the main game loop.
- game/score.py: Manages high scores.
- game/display.py: Manages the display and rendering.
- game/snake.py: Contains the snake-related functions and classes.
- game/obstacles.py: Handles obstacle creation and rendering.
- game/config.py: Contains the difficulty levels.
- requirements.txt: Lists the dependencies.

# License
This project is licensed under the MIT License.
