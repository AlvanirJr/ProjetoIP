import pygame
from pygame.locals import *

MAX_SHOTS      = 2
ALIEN_ODDS     = 22
BOMB_ODDS      = 60
ALIEN_RELOAD   = 12
SCREENRECT     = Rect(0, 0, 840, 480)
SCORE          = 0

class Explosion(pygame.sprite.Sprite):
    defaultlife = 12
    animcycle = 3
    images = []
    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.life = self.defaultlife
        self.rect.center = actor.rect.center

    def update(self):
        self.life = self.life - 1
        self.image = self.images[self.life/self.animcycle%2]
        if self.life <= 0: self.kill()