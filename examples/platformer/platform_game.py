import random
import pygame
import sys
# from examples.platformer import lib

from lib import Platform, Player

pygame.init()
 
HEIGHT = 1080
WIDTH = 810
ACC = 0.5
FRIC = -0.12
FPS = 60
HARDNESS = 6

def check(platform, groupies):
    if pygame.sprite.spritecollideany(platform,groupies):
        return True
    else:
        for entity in groupies:
            if entity == platform:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < 50) and (abs(platform.rect.bottom - entity.rect.top) < 50):
                return True
        C = False

def plat_gen():
    while len(platforms) < HARDNESS :
        width = random.randrange(50,100)
        p  = Platform(HEIGHT, WIDTH, None)      
        C = True
         
        while C:           
             p = Platform(HEIGHT, WIDTH, None)
             p.rect.center = (random.randrange(0, WIDTH - width),
                             random.randrange(-50, 0))
             C = check(p, platforms)
 
        platforms.add(p)
        all_sprites.add(p)
 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# bottom, override random sizing
PT1 = Platform(HEIGHT, WIDTH, None)
PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((255,0,0))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

P1 = Player(HEIGHT, WIDTH, ACC, FRIC)

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(PT1)

# create platforms for jumping
for x in range(random.randint(4,5)):
    C = True
    pl = Platform(HEIGHT, WIDTH, None)
    while C:
        pl = Platform(HEIGHT, WIDTH, None)
        C = check(pl, platforms)
    platforms.add(pl)
    all_sprites.add(pl)

while True:
    hits = pygame.sprite.spritecollide(P1 , platforms, False)
    P1.update(hits)
    # take player actions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump(hits)
        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_SPACE:
                P1.cancel_jump() 
    
    # randomly generate platforms as we go, removes lower platforms
    if P1.rect.top <= HEIGHT / 2:
        P1.pos.y += abs(P1.vel.y)
        for plat in platforms:
            plat.rect.y += abs(P1.vel.y)
            if plat.rect.top >= HEIGHT:
                plat.kill()

    plat_gen()

    # draw bottom
    displaysurface.fill((0,0,0))
    
    # collision
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        P1.draw(displaysurface)
        P1.move()
        
 
    pygame.display.update()
    FramePerSec.tick(FPS)
