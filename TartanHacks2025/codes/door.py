import pygame
from pygame.locals import *

class door:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/door.png")
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.playerHitDoor = False

    def draw(self, screen):
        if not self.playerHitDoor:
            screen.blit(self.image, self.rect)

    def checkTouch(self, player):
        #rect
        collided = self.rect.colliderect(player.rect) #check if collided with player
        #make the door disappear and change status
        if player.haskey1 and collided:
            self.image = None
            self.playerHitDoor = True
            player.hitDoor = True
            #now the scene should change
