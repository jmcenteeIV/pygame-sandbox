import pygame
import sys


from lib.player import Player
from lib.platform import Platform
 
pygame.init()
 
HEIGHT = 1080
WIDTH = 1920
ACC = 0.5
FRIC = -0.12
FPS = 60
 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

PT1 = Platform(HEIGHT, WIDTH)
P1 = Player(HEIGHT, WIDTH, ACC, FRIC)

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
     
    displaysurface.fill((0,0,0))
 
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        P1.move()
        P1.draw(displaysurface)
 
    pygame.display.update()
    FramePerSec.tick(FPS)
