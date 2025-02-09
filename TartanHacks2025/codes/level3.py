import pygame
from pygame.locals import *
import sys
import puzzles
import Sprites
import genai_texts
import os
import random
import level2
import ending
import fade_scene
import protag

def page3(screen, player, WIDTH, HEIGHT):
    # background
    background = Sprites.StoneBackground(WIDTH, HEIGHT) # Adjust path if needed
    foreground = Sprites.ForeGround(screen)

    foreground = Sprites.ForeGround(screen)
    player = protag.Player(20, 75)
    pot = Sprites.Pot(100, 200)
    key = puzzles.Puzzle1(200, 100)
    escapeDoor = key.door(300, 300)
    # escapeDoor.draw(screen)
    # key.draw(screen)
    running = True
    scene = 3
    get = False
    bubble_num = 0

    while running:
        player.speed = 10
        # Different background color for the new page
        scene1 = background.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (get):
                fade_scene.fade_to_next_scene(screen, pygame.time.Clock(), scene1)
                scene = 4

        if scene == 3:
            if not player.hasPot:
                pot.draw(screen)
            else:
                player.draw(screen)
            # door
            # escapeDoor.draw(screen)

            # draw player
            keys = pygame.key.get_pressed()
            player.move(keys, WIDTH, HEIGHT)  # Move player
            player.draw(screen)
            if not player.hasPot:
                pot.checkTouch(player, screen)
            else:
                for bubble in foreground.bubbles:
                    if bubble.checkTouch(player):
                        bubble_num += 1
                        foreground.bubbles.remove(bubble)
                        if bubble_num == 5:
                            get = True
                            scene = 4
                        # ending.page_end(screen, player, WIDTH, HEIGHT)

        elif scene == 4:
            player.speed = 0
            ending.page_end(screen, player, WIDTH, HEIGHT)

        # Display feedback
        # elif (not solved and submitted):
        #     unsolved_surface = font.render("Oops! Try again!", True, (255, 255, 0))
        #     screen.blit(unsolved_surface, (random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)))

        foreground.draw()
        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        pygame.time.Clock().tick(80)
