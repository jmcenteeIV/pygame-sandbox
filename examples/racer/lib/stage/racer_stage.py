import pygame
import sys
# from examples.platformer import lib

from lib import Car

pygame.init()

HEIGHT = 1080
WIDTH = 810
ACC = 0.5
FRIC = -0.12
FPS = 60

def main():
    FramePerSec = pygame.time.Clock()
 
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")

    player = Car(HEIGHT, WIDTH, FRIC, ACC)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    while True:
        # take player actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        displaysurface.fill((0,0,0))
        
        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)
            entity.draw(displaysurface)
            entity.move()

        pygame.display.update()
        FramePerSec.tick(FPS)

if __name__ == "__main__":
    main()


