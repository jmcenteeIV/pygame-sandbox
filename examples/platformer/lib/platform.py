import pygame
import random


class Platform(pygame.sprite.Sprite):
    def __init__(self, height: float, width: float):
        super().__init__()
        self.surf = pygame.Surface((random.randint(int(width*.03), int(width*.25)), 12))
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect(center = (random.randint(0,width-10),
                                                 random.randint(int(height*.05), int(height*.95))))

