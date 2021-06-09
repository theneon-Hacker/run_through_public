import pygame
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()



def mainMusic():
    
    main = pygame.mixer.Sound("sounds/background_music.ogg")
    main.set_volume(0.5)
    main.play(-1)

def mainStop():
    pygame.mixer.pause()

def mainCont():
    pygame.mixer.unpause()

def usingPortalSound():
    portal_using = pygame.mixer.Sound("sounds/using_portal.ogg")
    portal_using.play(0)


def activatedPortalSound():
    actived = pygame.mixer.Sound("sounds/portal_actived.ogg")
    actived.play(0)


def winMusic():
    win_music = pygame.mixer.Sound("sounds/win_music.ogg")
    win_music.set_volume(1)
    win_music.play(-1)


def menuMusic():
    pygame.init()
    pygame.mixer.init()
    menu = pygame.mixer.Sound("sounds/menu.ogg")
    menu.set_volume(1)
    menu.play(-1)



def begin():
    noise = pygame.mixer.Sound("sounds/noise_begin.ogg")
    noise.set_volume(0.7)
    noise.play(0)


def playButton():
    play_button = pygame.mixer.Sound("sounds/play_button.ogg")
    play_button.set_volume(1)
    play_button.play(0)


def menuStop():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.stop()


def enemyTarget():
    target = pygame.mixer.Sound("sounds/enemy_target.ogg")
    target.play(0)


def shoot():
    player_shoot = pygame.mixer.Sound("sounds/player_shoot.ogg")
    player_shoot.play(0)


def speedUp():
    speedup = pygame.mixer.Sound("sounds/speedUp.ogg")
    speedup.play(0)


def scoreAdded():
    __score__ = pygame.mixer.Sound("sounds/scoreAdded.ogg")
    __score__.play(0)


if __name__ == '__main__':
    raise FutureWarning('Better to import this file but you run this')
