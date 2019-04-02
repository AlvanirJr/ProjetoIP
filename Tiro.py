import pygame
from pygame.locals import *
MAX_SHOTS      = 2
ALIEN_ODDS     = 22
BOMB_ODDS      = 60
ALIEN_RELOAD   = 12
SCREENRECT     = Rect(0, 0, 840, 480)
SCORE          = 0

class Shot(pygame.sprite.Sprite):
    speed = -11
    images = []
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.midbottom = pos

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()
