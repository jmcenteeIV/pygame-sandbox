import random
import pygame
import sys
# from examples.platformer import lib

from lib import Platform, Player

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
PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((255,0,0))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

P1 = Player(HEIGHT, WIDTH, ACC, FRIC)

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(PT1)

for x in range(random.randint(5, 6)):
    pl = Platform(HEIGHT, WIDTH)
    platforms.add(pl)
    all_sprites.add(pl)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()
     
    displaysurface.fill((0,0,0))
 
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        P1.move()
        P1.draw(displaysurface)
        hits = pygame.sprite.spritecollide(P1 , platforms, False)
        P1.resolve_collisions(hits)
 
    pygame.display.update()
    FramePerSec.tick(FPS)
