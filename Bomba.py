import pygame
from pygame.locals import *
from Explosao import Explosion


MAX_SHOTS      = 2
ALIEN_ODDS     = 22
BOMB_ODDS      = 60
ALIEN_RELOAD   = 12
SCREENRECT     = Rect(0, 0, 840, 480)
SCORE          = 0

class Bomb(pygame.sprite.Sprite):
    speed = 12
    images = []
    def __init__(self, alien):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom + 5

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= 470:
            Explosion(self)
            self.kill()