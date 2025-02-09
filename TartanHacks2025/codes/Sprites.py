import pygame
from pygame.locals import *
import protag
import random
import puzzles

class Rock:
    def __init__(self, x, y):
        self.width = 60
        self.height = 60
        self.image = pygame.image.load("assets/rock.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(x, y))
    def draw(self, screen):
         # print("Image loaded successfully!", self.image)
         screen.blit(self.image, self.rect)

class Pot:
    def __init__(self, x, y):
        self.width = 60
        self.height = 60
        self.image = pygame.image.load("assets/pot.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(x, y))
    def draw(self, screen):
         # print("Image loaded successfully!", self.image)
         screen.blit(self.image, self.rect)
    def checkTouch(self, player, screen):
        #rect
        collided = self.rect.colliderect(player.rect) #check if collided with player
        #make the key disappear
        if collided:
            player.checkpot(screen)
            self.playerHasKey = True
            player.hasPot = True
            self.image = None

class WoodenTile:
     tileWidth, tileHeight = 50, 50
     def __init__(self, x, y):
        
        self.image = pygame.image.load("assets/wooden.png")

        self.image = pygame.transform.scale(self.image, (self.tileWidth, self.tileHeight))

        self.rect = self.image.get_rect(topleft=(x, y))

     def draw(self, screen):
        # print("Image loaded successfully!", self.image)
        screen.blit(self.image, self.rect)

class WoodenTileBackground:
     def __init__(self, width, height):
        self.image = pygame.image.load("assets/woodenBackground.png")

        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect(topleft=(0, 0))

     def draw(self, screen):
        # print("Image loaded successfully!", self.image)
        screen.blit(self.image, self.rect)
        return self.image

class StoneBackground:
     def __init__(self, width, height):
        self.image = pygame.image.load("assets/stoneBackground.png")

        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect(topleft=(0, 0))


     def draw(self, screen):
        
        screen.blit(self.image, self.rect)
        #print("Image loaded successfully!", self.image)
        return self.image

class Seaweed:
    width, height = 90,90
    def __init__(self, x, y):
        self.seaweed_count = 0
        
        self.image = pygame.image.load("assets/seaweed_1.png")

        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        # print("Image loaded successfully!", self.image)
        self.seaweed_count += 1
        screen.blit(self.image, self.rect)
        if(self.seaweed_count >= 15):
            self.image = pygame.image.load("assets/seaweed_2.png")

            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        if(self.seaweed_count >= 30):
            self.image = pygame.image.load("assets/seaweed_1.png")
            self.seaweed_count = 0
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            


class Bubble:
     def __init__(self):
        width, height = 25,25
        self.image = pygame.image.load("assets/Bubble.png")

        self.speed = random.randint(1,2)

        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect(topleft=(random.randint(0,800), 600))

        self.timecount = 0
        self.draw
     def draw(self, screen):
        # print("Image loaded successfully!", self.image)
        screen.blit(self.image, self.rect)
        
        self.timecount +=1
        if(self.timecount>70):
            self.timecount = 0
            bubble = Bubble()
            
        self.rect.y -= self.speed
     def checkTouch(self, player):
        #rect
        collided = self.rect.colliderect(player.rect) #check if collided with player
        #make the key disappear
        if collided:
            player.getBubble = True
            self.image = None
            return True
        return False
class ForeGround:
   def __init__(self, screen):    
      self.bubbles = [Bubble()]
      self.bubble_count = 0
      self.screen = screen
   def draw(self):
      self.bubble_count += 1
      for bubble in self.bubbles:
         bubble.draw(self.screen)
      if(self.bubble_count >= 50):
         self.bubbles.append(Bubble())
         self.bubble_count = 0
      transparent_surface = pygame.Surface((800, 600), pygame.SRCALPHA)
      transparent_surface.fill((0, 0, 40, 128))  # RGBA: 50% transparent blue
      self.screen.blit(transparent_surface, (0, 0))
      

