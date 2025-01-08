# Word Tracing Game

## Overview
The **Word Tracing Game** is an interactive application built using Python and OpenCV. Players trace shapes on an image while the application dynamically scores their performance based on specific color regions. This fun and engaging game promotes hand-eye coordination and provides real-time feedback.

---

## Features
- **Interactive Drawing**: Users can draw on the game canvas by clicking and dragging the mouse.
- **Dynamic Scoring**: The score updates based on the user’s interaction with predefined color regions.
- **Color Detection**: The program detects and processes pixel colors where the user interacts.
- **Customizable Image**: The application works with any image, resized to a 700x700 resolution.

---

## Setup and Requirements

### Dependencies
Ensure the following libraries are installed:
- `opencv-python`
- `numpy`
- `pandas`
- `pyautogui`

Install dependencies using pip:
```bash
pip install opencv-python numpy pandas pyautogui
```

### Image
The game requires an image file (`d.png`) in the working directory. Replace `d.png` with any desired image.

---

## Game Logic

### Drawing Function
The `draw_circle_with_drag` function allows users to draw red circles on the canvas by clicking and dragging the mouse. The score updates in real-time based on the color values at the drawn coordinates.

### Scoring System
- A predefined condition evaluates pixel colors (red, green, blue values).
- **Correct Interaction**: If specific RGB values (e.g., `R=4, G=255`) are detected, the score increases.
- **Incorrect Interaction**: Interaction outside valid regions doesn’t affect the score.

### Color Detection
The `score_function` calculates the RGB values of the pixel under the cursor and compares them to the target values. This ensures precise scoring.

---

## How to Play
1. Run the script.
2. The game window (`Word Tracing Game`) opens, displaying the image.
3. Use the left mouse button to trace the predefined regions.
4. The score updates as you interact with the correct regions.
5. Press `Esc` to exit the game.

---

## Code Details

### Variables
- **`score`**: Tracks the player's score.
- **`previous`**: Tracks the previous pixel’s RGB sum to avoid duplicate scoring.
- **`drawing`**: Boolean to track if the mouse is dragging.

### Key Functions
- **`draw_circle_with_drag`**: Handles mouse events for drawing.
- **`score_function`**: Calculates and updates the score based on pixel colors.

### Main Loop
The program continuously updates the game window, checks for user interactions, and processes the score in real time.

---

## Future Improvements
- Add multi-level challenges with different shapes and patterns.
- Enhance scoring logic to account for accuracy and timing.
- Display the score dynamically on the game window.
- Allow users to load custom images and set their own target regions.

---

## How to Run
Execute the script in your Python environment:
```bash
python word_tracing_game.py
```

---

## Acknowledgments
This project demonstrates Python’s capability in building interactive applications with OpenCV, showcasing an engaging way to combine programming with fun activities.

