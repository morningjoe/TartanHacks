import pygame
import openai
from openai import OpenAI
import requests
import json
import google.generativeai as genai

API_KEY = "AIzaSyCvEAFPwUCTRIl-BdsyCOeoZZFODf6rdKY"
genai.configure(api_key=API_KEY)

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Font for displaying text
font = pygame.font.Font(None, 36)

# Function to get AI-generated puzzle (riddle)
def generate_riddle():
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content("Create a puzzle for the player based on underwater themes, and the answer must be fish.")
    return response.text

# Initialize puzzle scene
puzzle_text = generate_riddle()
player_input = ""
solved = False

# Game loop
running = True
while running:
    screen.fill((0, 0, 50))  # Background color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Submit answer
                if "fish" in player_input.lower():  # Example condition (Replace with AI-checking logic)
                    solved = True
            elif event.key == pygame.K_BACKSPACE:
                player_input = player_input[:-1]  # Delete last character
            else:
                player_input += event.unicode  # Add typed character

    # Render puzzle text
    text_surface = font.render(puzzle_text, True, (255, 255, 255))
    screen.blit(text_surface, (50, 200))

    # Render player input
    input_surface = font.render("Your Answer: " + player_input, True, (0, 255, 0))
    screen.blit(input_surface, (50, 300))

    # Display feedback
    if solved:
        solved_surface = font.render("Correct! You solved the puzzle!", True, (255, 255, 0))
        screen.blit(solved_surface, (50, 400))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
