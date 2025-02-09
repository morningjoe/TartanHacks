import pygame
from pygame.locals import *
import sys
import protag
import puzzles
import Sprites

WIDTH, HEIGHT = 800, 600 #hardcoding bad

# Create a Transparent Surface for Fading
fade_surface = pygame.Surface((WIDTH, HEIGHT))
fade_surface.fill((0, 0, 0))  # Black fade by default

def fade_to_next_scene(screen, clock, scene1):
    for alpha in range(0, 256, 5):  # Increase alpha from 0 to 255
        fade_surface.set_alpha(alpha)  # Set transparency
        screen.blit(scene1, (0, 0))  # Keep the first scene visible
        screen.blit(fade_surface, (0, 0))  # Apply fade effect
        pygame.display.flip()
        clock.tick(70)  # Control fade speed
