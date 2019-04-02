
import pygame
import sys
from pygame.locals import *
import principal as pc


pygame.init()

def exitgame():
	pygame.quit()
	sys.exit()

clock = pygame.time.Clock()
pygame.display.set_caption('PASSAR OU MORRER')
width, height = 510, 480
screen = pygame.display.set_mode((width, height))

#Fundo do pygame
WHITE = (255, 255, 255)
#Tamanho da fonte
basicFont = pygame.font.SysFont(None, 40)

#Armazena o texto em uma variavel(Passando por parametro: TEXTO; VISIBILIDADE; COR
novo = basicFont.render('Novo jogo -> ( N )', True, (0,0,0))
instru = basicFont.render('Intrucoes -> ( I )', True, (0,0,0))
record = basicFont.render('Recordes -> ( R )', True, (0,0,0))
sair =  basicFont.render('Sair -> ( Esc )', True, (0,0,0))



def menu():

    clock.tick(60)

    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == pygame.QUIT:
                exitgame()

        #desenha os textos na tela
        screen.blit(novo, (width/4,10))
        screen.blit(instru, (width/4,100))
        screen.blit(record, (width/4,200))
        screen.blit(sair, (width/4,300))

         #Verifica se alguma tecla foi pressionada
        if event.type == KEYUP and event.key == K_n:
            pc.main()

        elif event.type == KEYUP and event.key == K_r:
            print "Recordes"

        elif event.type == KEYUP and event.key == K_i:
            print "Instrucoes"

        elif event.type == KEYUP and event.key == K_i:
            print "Instrucoes"

        #Atualiza a Tela
        pygame.display.flip()
        screen.fill(WHITE)

if __name__ == "__main__":
 	menu()