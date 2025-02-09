import pygame
from pygame.locals import *
import sys
import protag
import puzzles
import Sprites
import level2
import level3
import fade_scene
import door
import genai_texts

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("LiquidLabyrinth")

# Generate puzzles PLEASE REMOVE THIS
PUZZLE1 = "Say fish or else I will scream at you for eternity and forever and I don't like you"

# Create Player Instance
player = protag.Player(20, 75)

# Create puzzle1 instance
key = puzzles.Puzzle1(230, 370)
escapeDoor = key.door(400,300)
key.draw(screen)
escapeDoor.draw(screen)
#key = level1.Puzzle1()
#MAKE ROCKS HERE PLEASEEEEEEEEEEE
rock_coords = [[240,240], [180, 180], [180, 240], [120, 180], [100, 240],[120,300],[100,360],[120,420], [100, 480],[120, 540], [320, 200], [320, 280], [380, 200], [440, 200], [520, 290],[650, 400], [580, 380]]
rocks = []
for rock_coord in rock_coords:
    rocks.append(Sprites.Rock(rock_coord[0], rock_coord[1])) 
for rock in rocks:
    rock.draw(screen)
seaweed_coords = [[320, 380], [20, 200], [20,300], [20,400], [400, 50], [500, 60], [200, 340]]
seaweeds = []
for seaweed_coord in seaweed_coords:
    seaweeds.append(Sprites.Seaweed(seaweed_coord[0], seaweed_coord[1]))
# background
background = Sprites.WoodenTileBackground(WIDTH, HEIGHT) # Adjust path if needed

foreground = Sprites.ForeGround(screen)

scene = 1
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (player.hitDoor and scene == 1):
            scene1 = pygame.image.load("assets/woodenBackground.png")
            scene1 = pygame.transform.scale(scene1, (WIDTH, HEIGHT))
            fade_scene.fade_to_next_scene(screen, clock, scene1)
            scene = 2

    if (player.hitDoor and scene == 1):
        player.speed = 0

    if scene == 1:
        background.draw(screen)
        key.draw(screen)
        
        #draw seaweed
        for seaweed in seaweeds:
            seaweed.draw(screen)
        
        # draw player
        keys = pygame.key.get_pressed()
        player.move(keys, WIDTH, HEIGHT)  # Move player
        player.draw(screen)  # Draw player (must be AFTER filling the screen)
        #draw rocks
        for rock in rocks:
            rock.draw(screen)
            player.collision(rock, keys, WIDTH, HEIGHT)
        escapeDoor.draw(screen)
        # if no key, door is a obstacle
        if(not player.haskey1):
            player.collision(escapeDoor, keys, WIDTH, HEIGHT)

        if player.haskey1:
            escapeDoor.checkTouch(player)
        else:
            key.checkTouch(player)

    elif scene == 2:
        player.speed = 0
        level2.page2(screen, player, WIDTH, HEIGHT)
        # scene = 3

    # elif scene == 3:
    #     player.speed = 3
    #     level3.page3(screen, WIDTH, HEIGHT)



    foreground.draw()
    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(80)


pygame.quit()
