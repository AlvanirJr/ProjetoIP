
import pygame
from pygame.locals import *

class carregarsom:
    def play(self): pass

    def load_sound(file):
        if not pygame.mixer: return carregarsom()
        file = os.path.join('data', file)
        try:
            sound = pygame.mixer.Sound(file)
            return sound
        except pygame.error:
            print 'impossivel de carregar,', file
        return carregarsom()