import pygame
import sys
from pygame.locals import *

# initializes pygame class
pygame.init()

# creates a 2D game
vec = pygame.math.Vector2

# creating game screen 
HEIGHT = 450
WIDTH = 400
# creating realistic movement
# ACC = accleration
# FRIC = friction
ACC = 0.5
FRIC = -0.12
# controling frame rate
FPS = 60

# used to control the screen frames per second
FramePerSec = pygame.time.Clock()

# setting the screen shape
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))

# what will be display at the top of the window
pygame.display.set_caption("Game")

"""
Creating Player object and Platform objects that the player interacts with 
"""

class Player(pygame.sprite.Sprite):
    """
     Player object controlled by user
    """
    def __init__(self):
        super().__init__()
        # creating a surface object for Player class with a fixed size
        self.surf = pygame.Surface((30, 30))
        # giving a color to the Player object in RGB format
        self.surf.fill((128, 255, 40))
        # giving the Player object a rectangle shape, center is used to define the starting point of the object
        # all objects starting point is top-left corner of screen (0, 0)
        self.rect = self.surf.get_rect(center=(10, 420))

        # creating player movement
        # vec is used to create variables with 2 dimensions
        # vec parameters use X/Y axis since its 2D
        self.pos = vec((10, 385))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        def move(self):
            """
             allows control of player movement
            """
            # re-sets value of acc to 0
            self.acc = vec(0, 0)
            
            # variable to obtain keyboard presses
            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[K_LEFT]:
                self.acc.x = -ACC
            if pressed_keys[K_RIGHT]:
                self.acc.x = ACC

class Platform(pygame.sprite.Sprite):
    """
     Platforms player jumps over
    """
    def __init__(self):
        super().__init__()
        # creating a surface object for Platform class with a fixed size
        self.surf = pygame.Surface((WIDTH, 20))
        # giving a color to the Platform object in RGB format
        self.surf.fill((255, 0, 0))
        # giving the Platform object a rectangle shape, center is used to define the starting point of the object
        # all objects starting point is top-left corner of screen (0, 0)
        self.rect = self.surf.get_rect(center= (WIDTH / 2, HEIGHT - 1 ))

PT1 = Platform()
P1 = Player()

"""
Creating the game loop and introducing Sprite Groups

Sprite = computer graphics term for any object on the screen that can move around, in pygame
Sprite is a class designed to be a base class for all your game objects which isn't meant to be used on it's own, but has several methods
to help work with different Group classes. 

Group = A simple container class that holds Sprites
"""

# creating sprites and adding them to a group
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # refreshes the screen with each iteration
    displaysurface.fill((0, 0, 0))

    # iterate through the all_sprites group and drawing them all to the screen
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    # pushes all the changes to the screen
    pygame.display.update()

    # uses the Clock() object to limit the game loop to refresh 60 times per second
    FramePerSec.tick(FPS)