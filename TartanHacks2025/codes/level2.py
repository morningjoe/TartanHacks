import pygame
from pygame.locals import *
import sys
import puzzles
import Sprites
import genai_texts
import os
import random
import fade_scene
import level3
import random

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ''

    for word in words:
        test_line = current_line + ' ' + word if current_line else word
        test_width, _ = font.size(test_line)

        if test_width <= max_width:  # If the line fits within the width
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:  # Add the last line
        lines.append(current_line)

    return lines

def page2(screen, player, WIDTH, HEIGHT):
    # background
    font = pygame.font.Font(None, 36)
    background = Sprites.StoneBackground(WIDTH, HEIGHT) # Adjust path if needed

    riddles = {1: "I live in a shell, but I'm not a turtle. You might hear the ocean if you hold me to your ear. What am I?",
               2: "I have a mouth but I never speak. I have a bed but never sleep. What am I?",
               3: "What do you call a fish with no eyes?",
               4: "What letter holds the most water?"}
    answers = {1: "seashell",
               2: "river",
               3: "fsh",
               4: "c"}


    # Initialize puzzle scene
    puzzleNumber = random.randint(1, len(riddles))
    puzzle_text = riddles[puzzleNumber]
    puzzle_answer = answers[puzzleNumber]
    lines = wrap_text(puzzle_text, font, WIDTH - 20)
    player_input = ""
    solved = False
    foreground = Sprites.ForeGround(screen)
    running = True
    submitted = False
    scene = 2

    while running:
        # Different background color for the new page
        scene1 = background.draw(screen)

        # run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Submit answer
                    submitted = True
                    if puzzle_answer in player_input.lower():  # Example condition (Replace with AI-checking logic)
                        solved = True
                elif event.key == pygame.K_BACKSPACE:
                    player_input = player_input[:-1]  # Delete last character
                else:
                    player_input += event.unicode  # Add typed character
            if solved == True:
                fade_scene.fade_to_next_scene(screen, pygame.time.Clock(), scene1)
                scene = 3

        if scene == 3:
            level3.page3(screen, player, WIDTH, HEIGHT)

        # keys
        keys = pygame.key.get_pressed()

        # Render puzzle text
        y_offset = 50  # Start position for the text
        for line in lines:
            rendered_text = font.render(line, True, (255, 255, 255))  # Black text
            screen.blit(rendered_text, (30, y_offset))  # Draw at position (10, y_offset)
            y_offset += rendered_text.get_height()  # Move to the next line

        # Render player input
        input_surface = font.render("Your Answer: " + player_input, True, (0, 255, 0))
        screen.blit(input_surface, (50, 300))

        # Display feedback
        if solved:
            solved_surface = font.render("Correct! You solved the puzzle!", True, (255, 255, 0))
            screen.blit(solved_surface, (50, 400))
            running = False
            #remove all text and end level 2 to set up for level 3
            #then return to main and move to puzzle 3
        elif (not solved and submitted):
            unsolved_surface = font.render("Oops! Try again!", True, (255, 255, 0))
            screen.blit(unsolved_surface, (random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)))
        # draw key
        # key.draw(screen)
        # key.checkTouch(player)
        foreground.draw()
        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        pygame.time.Clock().tick(80)
