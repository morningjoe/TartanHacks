import pygame
from pygame.locals import *
import sys
import puzzles
import Sprites
import genai_texts
import os
import random
import level2

def page_end(screen, player, WIDTH, HEIGHT):
    # background
    font = pygame.font.Font(None, 60)
    font2 = pygame.font.Font(None, 36)
    background = Sprites.StoneBackground(WIDTH, HEIGHT) # Adjust path if needed

    # Initialize puzzle scene
    congrats_text = "Congrats! You've escaped!"
    instruction_text = "Press Space to exit the game"
    lines = level2.wrap_text(instruction_text, font, WIDTH - 20)
    player_input = ""
    solved = False
    foreground = Sprites.ForeGround(screen)
    running = True
    submitted = False

    while running:
        # get keyboard input
        keys = pygame.key.get_pressed()

        # Different background color for the new page
        background.draw(screen)

        # run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_SPACE]:
                pygame.quit()
                sys.exit()

        # Render puzzle text
        y_offset = 500  # Start position for the text
        for line in lines:
            rendered_text = font2.render(line, True, (255, 255, 255))  # Black text
            screen.blit(rendered_text, (30, y_offset))  # Draw at position (10, y_offset)
            y_offset += rendered_text.get_height()  # Move to the next line

        # Display feedback
        solved_surface = font.render(congrats_text, True, (255, 255, 0))
        screen.blit(solved_surface, (100, 250))

        foreground.draw()
        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        pygame.time.Clock().tick(60)
