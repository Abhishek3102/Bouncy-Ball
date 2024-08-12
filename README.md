# Bounce Ball Game

This is a simple Python-based bounce ball game created using the Turtle graphics module. The player controls a turtle-shaped object to collide with various shapes that randomly appear on the screen. Each shape has a different point value, and the player's goal is to score as many points as possible by collecting these shapes.

## How to Play

- **Controls**:
  - Use the **Left Arrow** key to move left.
  - Use the **Right Arrow** key to move right.
  - Use the **Up Arrow** key to move up.
  - Use the **Down Arrow** key to move down.

- **Objective**:
  - Control the turtle and collect the falling shapes to score points.
  - The game ends when the player decides to stop playing.

- **Scoring**:
  - **Square**: 10 points
  - **Circle**: 20 points
  - **Arrow**: 30 points

## Features

- **Randomized Shapes**: Shapes with different colors and forms randomly appear on the screen.
- **Gravity**: The turtle and shapes are affected by gravity, adding to the challenge.
- **Collision Detection**: The game detects collisions between the player and shapes, updating the score accordingly.
- **Dynamic Difficulty**: The speed of the shapes increases as the player collects more shapes.

## Requirements

- Python 3.x
- Turtle module (usually included with Python)

## Installation

1. Clone this repository:
    ```bash
    git clone (https://github.com/Abhishek3102/Bouncy-Ball.git)
    ```

2. Run the game:
    ```bash
    python bounce_ball_game.py
    ```

## How It Works

- The player starts with a turtle-shaped object positioned at the bottom of the screen.
- Random shapes (square, circle, arrow, etc.) appear at random positions on the screen and fall downward due to gravity.
- The player controls the turtle using the arrow keys to collect these shapes.
- If the player collides with a shape, it disappears, and the player gains points based on the shape's type.
- The difficulty of the game increases as the gravity strength increases when shapes are collected.

## Customization

You can customize the game by modifying the following parameters in the code:

- **num_shapes**: The number of shapes that appear on the screen at the start.
- **possible_shapes**: The types of shapes that can appear.
- **colors**: The colors available for the shapes.
- **gravity**: The initial gravity strength affecting the turtle and shapes.
- **speed_increase**: The amount by which gravity increases after each successful collision.

## License

This project is licensed under the MIT License.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.
