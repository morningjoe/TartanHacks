import pygame
from pygame.locals import *
import door

class Puzzle1:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/key.png")
        self.image = pygame.transform.scale(self.image, (30, 60))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.playerHasKey = False

    def door(self, x, y):
        escapeDoor  = door.door(x, y)
        return escapeDoor

    def draw(self, screen):
        if not self.playerHasKey:
            screen.blit(self.image, self.rect)

    def checkTouch(self, player):
        #rect
        collided = self.rect.colliderect(player.rect) #check if collided with player
        #make the key disappear
        if collided:
            self.playerHasKey = True
            player.haskey1 = True
            self.image = None

        #now the player should move to the chest or the other target to solve this puzzle

print("puzzle has ran")