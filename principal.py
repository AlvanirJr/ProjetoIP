# Importa os modelos basicos do pygame


import random, os.path
import pygame
from pygame.locals import *
import jogador as cs
import alien as al
import Explosao as ex
import Tiro as ti
import Bomba as bm
import Pontuacao as pt
import menu as mn

# Constantes
MAX_SHOTS      = 2
ALIEN_ODDS     = 10
BOMB_ODDS      = 75
ALIEN_RELOAD   = 40
SCREENRECT     = Rect(0, 0, 840, 480)
SCORE          = 0





# Carregar modelo padrao
if not pygame.image.get_extended():
    raise SystemExit, "Desculpe, modulo de imagem estendida necessaria"


def load_image(file):
    "Carrega a Imagem e prepara para o jogo"
    file = os.path.join('data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit, 'Nao foi possivel carregar a imagem "%s" %s'% (file, pygame.get_error())
    return surface.convert()


def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs


class dummysound:
    def play(self): pass





def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os.path.join('d', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print 'Impossivel de carregar', file
    return dummysound()


def drawText(text, font, surface, x, y, color):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def texts(score,screen):
   font=pygame.font.Font(None,30)
   scoretext=font.render(score, 1,(255,255,255))
   screen.blit(scoretext, (0, 200))

def main(winstyle=0):
    # Initialize pygame
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print 'Warning, no sound'
        pygame.mixer = None

    # Mdodo de exibicao
    winstyle = 0  #tela
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    # Carregamento das imagens


    img = load_image('player1.gif')
    cs.Player.images = [img, pygame.transform.flip(img, 1, 0)]
    img = load_image('explosion1.gif')
    ex.Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
    al.Alien.images = load_images('alien1.gif', 'alien2.gif', 'alien3.gif')
    bm.Bomb.images = [load_image('bomb.gif')]
    ti.Shot.images = [load_image('shot.gif')]


    # decorate the game window
    icon = pygame.transform.scale(cs.Player.images[0], (32, 32))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('PASSAR EM IP OU MORRER')
    pygame.mouse.set_visible(0)

    # Fundo
    bgdtile = load_image('background.gif')
    background = pygame.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()


    # Carrega os efeitos sonoros
    boom_sound = load_sound('boom.wav')
    shoot_sound = load_sound('car_door.wav')
    if pygame.mixer:
        music = os.path.join('data', 'bg2.mp3')
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)



    # Initialize Game Groups
    aliens = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()
    lastalien = pygame.sprite.GroupSingle()

    ####atribuir grupos padrao para cada classe Sprite
    cs.Player.containers = all
    al.Alien.containers = aliens, all, lastalien
    ti.Shot.containers = shots, all
    bm.Bomb.containers = bombs, all
    ex.Explosion.containers = all
    pt.Score.containers = all


    # Criar Alguns valores iniciais
    global Score
    alienreload = ALIEN_RELOAD
    clock = pygame.time.Clock()

    # initialize our starting sprites
    global SCORE
    player = cs.Player()
    al.Alien()
    if pygame.font:
        all.add(pt.Score())

    score = pt.Score()

    while player.alive():



        for event in pygame.event.get():
            if event.type == QUIT or \
                    (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
        keystate = pygame.key.get_pressed()

        all.clear(screen, background)

        all.update()

        # Entrada do jogador

        direction = keystate[K_RIGHT] - keystate[K_LEFT]
        player.move(direction)
        firing = keystate[K_SPACE]
        if not player.reloading and firing and len(shots) < MAX_SHOTS:
            ti.Shot(player.gunpos())
            shoot_sound.play()
        player.reloading = firing

        # Criando novo inimigo
        if alienreload:
            alienreload = alienreload - 1
        elif not int(random.random() * ALIEN_ODDS):
            al.Alien()
            alienreload = ALIEN_RELOAD

        # Soltar bomba
        if lastalien and not int(random.random() * BOMB_ODDS):
            bm.Bomb(lastalien.sprite)


        # detectar colisoes
        for alien in pygame.sprite.spritecollide(player, aliens, 1):
            boom_sound.play()
            ex.Explosion(alien)
            ex.Explosion(player)
            SCORE = SCORE + 1
            print "Game over"
            player.kill()
            pygame.display.delay(3000)


        for alien in pygame.sprite.groupcollide(shots, aliens, 1, 1).keys():
            boom_sound.play()
            ex.Explosion(alien)
            SCORE = SCORE  + 1
            print SCORE



        for bomb in pygame.sprite.spritecollide(player, bombs, 1):
            boom_sound.play()
            ex.Explosion(player)
            ex.Explosion(bomb)
            player.kill()
            print "Game over"
            pygame.display.delay(3000)




        #drawText("Score: %s" % (SCORE),pygame.font.Font(None,50),screen, 0,0,(255,255,255))
        #texts("Score: %s" % (SCORE), screen)
        font=pygame.font.Font(None,30)
        scoretext=font.render("Score: %s" % (SCORE), 1,(255,255,255))
        screen.blit(scoretext, (0, 0))


        # desenhar a cena
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # cap the framerate
        clock.tick(60)

    if pygame.mixer:
        pygame.mixer.music.fadeout(1000)
    pygame.time.wait(1000)




# Chamanndo a funcaoo
#if __name__ == '__main__': main()
