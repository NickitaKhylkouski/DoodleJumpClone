# Doodle Jump Clone
This project is a Python-based clone of the popular mobile game Doodle Jump. It's implemented using Pygame and provides a fun, endless jumping experience.
## Game Description
In this game, you control a character (the "Doodle") that automatically jumps. Your goal is to guide the Doodle onto platforms to jump higher and higher, earning points as you ascend. The game features:
- Randomly generated platforms
- Springs that give extra bounce
- Scoring system
- Game over when falling off the bottom of the screen
## Installation
To run this game, you'll need Python and Pygame installed on your system.
1. First, ensure you have Python 3.10 or newer installed. You can download it from [python.org](https://www.python.org/downloads/).
2. Install Pygame using pip:
pip install pygame

3. Clone this repository or download the source code.
## How to Play
1. Run the game by executing the `main.py` file:
python main.py

2. Use the left and right arrow keys (or 'A' and 'D' keys) to move the Doodle left and right.
3. Jump on platforms to go higher.
4. Try to achieve the highest score possible!
5. Press 'R' to restart the game at any time.
## Project Structure
- `main.py`: The main game loop and initialization.
- `sprites/`:
- `doodle.py`: The player character class.
- `platforms.py`: The platform class.
- `Spring.py`: The spring power-up class.
- `game.py`: Contains the Score and GameOver classes.
- `assets/`: Contains game assets like images and fonts.
## Dependencies
This project requires:
- Python 3.10+
- Pygame 2.6.1
## Contributing
Feel free to fork this project and submit pull requests with improvements or bug fixes!
## Acknowledgements
This game is inspired by the original Doodle Jump game created by Lima Sky.
