import random, os.path
import pygame
from pygame.locals import *
import jogador as cs
import alien as al
import Explosao as ex
import Tiro as ti
import Bomba as bm
import Pontuacao as pt

MAX_SHOTS      = 2
ALIEN_ODDS     = 22
BOMB_ODDS      = 60
ALIEN_RELOAD   = 12
SCREENRECT     = Rect(0, 0, 840, 480)
SCORE          = 0

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None,40)
        self.font.set_italic(1)
        self.color = 255, 255, 255
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 450)


    def update(self):
        print "update"
        if SCORE != self.lastscore:
            print "entrou " + str(SCORE)
            self.lastscore = SCORE
            msg = "Pontos: %d" % (SCORE)
            self.image = self.font.render("", 0, self.color)
