import pygame
from pygame.locals import *
import random
SCREENRECT     = Rect(0, 0, 840, 480)
class Alien(pygame.sprite.Sprite):
    speed = 17
    animcycle = 15
    images = []
    def __init__(self):
        """type: Alien"""
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((1,1)) * Alien.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing;
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1
        self.image = self.images[self.frame/self.animcycle%3]
